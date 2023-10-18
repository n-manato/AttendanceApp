from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from mylogin.models import User, Subject, Department
from .models import AttendanceInfo, Attend, Hour, Total
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from datetime import datetime, timedelta, date
import json
from django.db.models import Q


def welcome_view(request):
    return render(request, 'welcome.html')


@user_passes_test(lambda u: u.groups.filter(name='Student').exists(), login_url='')
def Students_list(request):
    # 必要なデータを取得してコンテキストに追加する
    user = request.user
    subjects = user.Subject.all()
    today_date = date.today()
    next_date = today_date + timedelta(1)
    selected_subject = subjects.last()
    selected_start = today_date.strftime("%Y-%m-%d")
    selected_end = next_date.strftime("%Y-%m-%d")
    attendanceinfo = []
    dict_attend = {}
    student = user.full_name
    unique_dates = None
    unique_students = None
    if request.method == "POST" or request.method == "GET":
        if request.method != "GET":
            selected_subject = Subject.objects.get(
                subject=request.POST.get('subject'))
            selected_start = request.POST.get('start_date')
            selected_end = request.POST.get('end_date')
        attendanceinfo = AttendanceInfo.objects.filter(Q(date__gte=selected_start) & Q(
            date__lte=selected_end), subject=selected_subject, student=User.objects.get(full_name=student)).order_by('date', 'time')
        unique_dates = sorted(set(attendance.date.strftime('%Y-%m-%d')
                                  for attendance in attendanceinfo))
        unique_students = set(
            attendance.student.full_name for attendance in attendanceinfo)
        for students in unique_students:
            dict_attend[students] = {}
            dict_attend[students]['total'] = 0
            for data in attendanceinfo:
                dict_attend[students][data.date.strftime('%Y-%m-%d')] = {}
            for data in attendanceinfo:
                dict_attend[students][data.date.strftime('%Y-%m-%d')][data.time.hour] = {'first_half': None,
                                                                                         'latter_half': None,
                                                                                         }
        for data in attendanceinfo:
            dict_attend[data.student.full_name][data.date.strftime('%Y-%m-%d')][data.time.hour] = {'first_half': data.first_half.type,
                                                                                                   'latter_half': data.latter_half.type,
                                                                                                   }
            if selected_subject.subject != 'HR':
                if data.first_half.type == '欠席':
                    dict_attend[data.student.full_name]['total'] += 1
                if data.latter_half.type == '欠席':
                    dict_attend[data.student.full_name]['total'] += 1
            else:
                if data.first_half.type == '欠席':
                    dict_attend[data.student.full_name]['total'] += 1

    menu_items = [
        {'name': 'Logout', 'url': reverse('loginapp:logout')},
        {'name': 'Students List', 'url': reverse('ATbook:Studentslist')},
    ]
    context = {
        'subjects': subjects,
        'unique_date': unique_dates,
        'selected_subject': selected_subject,
        'selected_start': selected_start,
        'selected_end': selected_end,
        'attendanceinfo': dict_attend,
        'student': student,
        'menu_items': menu_items,
    }
    return render(request, 'Studentslist.html', context)


@user_passes_test(lambda u: u.groups.filter(name__in=['HomeroomTeacher', 'SubjectTeacher']).exists(), login_url='')
def Teachers_list(request):
    # 必要なデータを取得してコンテキストに追加する
    user = request.user
    subjects = user.Subject.all()
    today_date = date.today()
    next_date = today_date + timedelta(1)
    selected_subject = subjects.last()
    selected_start = today_date.strftime("%Y-%m-%d")
    selected_end = next_date.strftime("%Y-%m-%d")
    attendanceinfo = []
    dict_attend = {}
    th = {}
    teacher = user.full_name
    unique_dates = None

    if request.method == "POST" or request.method == "GET":
        if request.method != "GET":
            selected_subject = Subject.objects.get(
                subject=request.POST.get('subject'))
            selected_start = request.POST.get('start_date')
            selected_end = request.POST.get('end_date')
        attendanceinfo = AttendanceInfo.objects.filter(Q(date__gte=selected_start) & Q(
            date__lte=selected_end), subject=selected_subject).order_by('date', 'time')
        unique_dates = sorted(set(attendance.date.strftime('%Y-%m-%d')
                                  for attendance in attendanceinfo))
        unique_hour = sorted(
            set(attendance.time.hour for attendance in attendanceinfo))
        unique_students = set(
            attendance.student.full_name for attendance in attendanceinfo)

        for dated in unique_dates:
            th[dated] = []  # 各日付をキーとした空のリストを th ディクショナリに追加

        for data2 in attendanceinfo:
            dated = data2.date.strftime('%Y-%m-%d')  # data2 の日付をフォーマット
            hour = data2.time.hour  # data2 の時間を取得

            if hour not in th[dated]:
                th[dated].append(hour)  # リストに時間を追加

        for data in unique_students:
            dict_attend[data] = {}
            for dates in unique_dates:
                dict_attend[data]['total'] = 0
                dict_attend[data][dates] = {}
            for data2 in attendanceinfo:
                dates = data2.date.strftime('%Y-%m-%d')  # data2 の日付をフォーマット
                hour = data2.time.hour  # data2 の時間を取得
                if hour not in dict_attend[data][dates]:
                    dict_attend[data][dates][hour] = {'first_half': None,
                                                    'latter_half': None,
                                                    }

        for data in attendanceinfo:
            dict_attend[data.student.full_name][data.date.strftime('%Y-%m-%d')][data.time.hour] = {
                'first_half': data.first_half.type, 'latter_half': data.latter_half.type, }
            print(dict_attend)

            if selected_subject.subject != 'HR':
                if data.first_half.type == '欠席':
                    dict_attend[data.student.full_name]['total'] += 1
                if data.latter_half.type == '欠席':
                    dict_attend[data.student.full_name]['total'] += 1
            else:
                if data.first_half.type == '欠席':
                    dict_attend[data.student.full_name]['total'] += 1
    menu_items = [
        {'name': 'Logout', 'url': reverse('loginapp:logout')},
        {'name': 'Teachers List', 'url': reverse('ATbook:Teacherslist')},
        {'name': 'Attend Definition', 'url': reverse('ATbook:Attenddef')},
        {'name': 'Admin', 'url': reverse('admin:index')},
    ]
    context = {
        'subjects': subjects,
        'th': th,
        'selected_subject': selected_subject,
        'selected_start': selected_start,
        'selected_end': selected_end,
        'attendanceinfo': dict_attend,
        'teacher': teacher,
        'menu_items': menu_items,
    }
    return render(request, 'Teacherslist.html', context)


@user_passes_test(lambda u: u.groups.filter(name__in=['HomeroomTeacher', 'SubjectTeacher']).exists(), login_url='')
def Attend_def(request):
    # 必要なデータを取得してコンテキストに追加する
    students = []
    many_date = []
    dict_attend = {}
    user = request.user
    success_message = request.session.get('message')
    request.session['message'] = None
    subjects = user.Subject.all()
    test1 = Subject.objects.get(pk=1)
    selected_subjects = test1.related_Subject.all()
    print(selected_subjects)
    teacher = user.full_name
    selected_subject = {}
    submit_teacher = {}
    selected_date = None
    dates = AttendanceInfo.objects.values_list('date', flat=True).distinct()
    many_date = [date.strftime("%Y-%m-%d") for date in dates]
    today_date = date.today().strftime("%Y-%m-%d")

    if today_date not in many_date:
        many_date.append(today_date)
    messeage = None
    selected_date = request.session.get("selected_date")
    if request.session.get("selected_date") == None:
        selected_date = today_date
    request.session["selected_date"] = today_date
    selected_department = 'CS'
    selected_department = Department.objects.get(name=selected_department)
    dict_attend = {}
    students = User.objects.filter(
        departments__name=selected_department, groups__name='Student')
    full_names = [student.full_name for student in students]
    time_hours = Hour.objects.all()
    time_hour_name = [time_hour.hour for time_hour in time_hours]

    # POST時の処理
    if request.method == "POST" or request.method == 'GET':
        if request.method == "POST":
            success_message = None
        many_date = [date.strftime("%Y-%m-%d") for date in dates]
        today_date = date.today().strftime("%Y-%m-%d")
        if today_date not in many_date:
            many_date.append(today_date)
        selected_department = 'CS'
        selected_department = Department.objects.get(name=selected_department)
        dict_attend = {}

        if 'date-select' in request.POST or request.method == 'GET':
            # POSTリクエストがドロップダウンから送信された場合の処理
            if request.POST.get('date-select') == "" and request.method != 'GET':
                selected_subject = None
                students = None
            else:
                if request.method != 'GET':
                    selected_date = request.POST.get('date-select')
                attendance_info = AttendanceInfo.objects.filter(
                    date=selected_date, student__departments=selected_department).order_by('time')
                students = User.objects.filter(
                    departments__name=selected_department, groups__name='Student')

                time_data = Hour.objects.all()  # Hourモデルから時間データを取得
                for student in students:
                    if student.full_name not in dict_attend:
                        dict_attend[student.full_name] = {}
                        total_late = 0
                        total_leave = 0
                        total_absent = 0
                        total_present = 0
                    totals = Total.objects.filter(student=student)
                    dict_attend[student.full_name]["total"] = "0/0/0"

                    for total in totals:
                        total_late += total.late
                        total_leave += total.leave
                        total_absent += total.absent
                        total_present += total.present
                    dict_attend[student.full_name]["total"] = f"{total_late}/{total_leave}/{total_absent}"

                    for times in time_data:
                        if times.hour not in dict_attend[student.full_name]:
                            dict_attend[student.full_name][times.hour] = {
                                'first_half': [], 'latter_half': []}
                            for data in attendance_info:
                                if times == data.time and student == data.student:
                                    dict_attend[student.full_name][times.hour]['first_half'].append(
                                        data.first_half.type)
                                    dict_attend[student.full_name][times.hour]['latter_half'].append(
                                        data.latter_half.type)
                                    selected_subject[times.hour] = data.subject.subject
                                    submit_teacher[times.hour] = data.teacher.full_name

                # ここに遅刻、早退、欠席のフラグを立てるプログラムを生成する

        elif 'submit' in request.POST.get('action'):
            print(request.POST)
            json_data = json.loads(request.POST.get('data'))
            selected_date = request.POST.get('selected_date')
            success_message = "Data submitted successfully."
            request.session['message'] = success_message
            request.session["selected_date"] = selected_date
            print(selected_date)
            subject_instance = None
            for item in json_data:
                student = item['student']
                subject_instance = item['subject']
                print(subject_instance)
                if subject_instance != '':
                    subject_instance = Subject.objects.get(
                        subject=subject_instance)
                    sub_teacher = request.user
                    hour = item['hour']
                    first_half = item['first_half']
                    if first_half == '1':
                        first_half = Attend.objects.get(type='出席')
                    elif first_half == '2':
                        first_half = Attend.objects.get(type='欠席')
                    else:
                        first_half = None

                    latter_half = item['latter_half']
                    if latter_half == '1':
                        latter_half = Attend.objects.get(type='出席')
                    elif latter_half == '2':
                        latter_half = Attend.objects.get(type='欠席')
                    else:
                        latter_half = None
                    print(student)
                    print(hour)
                    print(first_half)
                    print(latter_half)
                    if first_half is None or latter_half is None:
                        condition = Q(student__full_name=student) & Q(
                            time__hour=hour) & Q(date=selected_date)
                        AttendanceInfo.objects.filter(condition).delete()
                        print('データセットを削除しました。')
                    else:
                        # どちらかが None でない場合、データを更新または作成
                        AttendanceInfo.objects.update_or_create(
                            student=User.objects.get(full_name=student),
                            time=Hour.objects.get(hour=hour),
                            teacher=sub_teacher,
                            date=selected_date,
                            defaults={
                                'first_half': first_half,
                                'latter_half': latter_half,
                                'subject': subject_instance,
                            }
                        )
                else:
                    student = item['student']
                    hour = item['hour']
                    condition = Q(student__full_name=student) & Q(
                        time__hour=hour) & Q(date=selected_date)
                    AttendanceInfo.objects.filter(condition).delete()
                    print('データセットを削除しました。')

            for student in students:
                count = 0
                first_flag = 0
                middle_flag = 0
                last_flag = 0
                late = 0
                leave = 0
                absent = 0
                present = 0

                totalling = AttendanceInfo.objects.filter(
                    date=selected_date, student=student).order_by('time')
                print(student)
                for data in totalling:
                    print(data.first_half.type)
                    if count == 0 and data.first_half.type == '欠席':
                        first_flag = 1
                    elif count == len(totalling) - 1 and data.latter_half.type == '欠席':
                        last_flag = 1
                    elif data.latter_half.type == '出席' or data.first_half.type == '出席':
                        middle_flag = 1
                    count += 1
                print(count)
                print(first_flag)
                print(last_flag)
                print(last_flag)
                if middle_flag == 1:
                    if first_flag + last_flag == 2:
                        print('遅刻&早退')
                        late = 1
                        leave = 1
                    elif first_flag == 1:
                        print('遅刻')
                        late = 1
                    elif last_flag == 1:
                        print('早退')
                        leave = 1
                elif first_flag + last_flag == 2 and middle_flag == 0:
                    print('休み')
                    absent = 1
                else:
                    print('出席')
                    present = 1
                Total.objects.update_or_create(
                    student=student,
                    date=selected_date,
                    defaults={
                        'late': late,
                        'leave': leave,
                        'absent': absent,
                        'present': present,
                    }
                )

                # データベースへの格納が成功したかどうかを確認
            redirect_url = reverse('ATbook:Attenddef')
            print(redirect_url)
            response_data = {
                'redirect': redirect_url,  # リダイレクト先のURL
                'success_message': success_message,
            }
            return JsonResponse(response_data, safe=False)

    menu_items = [
        {'name': 'Logout', 'url': reverse('loginapp:logout')},
        {'name': 'Teachers List', 'url': reverse('ATbook:Teacherslist')},
        {'name': 'Attend Definition', 'url': reverse('ATbook:Attenddef')},
        {'name': 'Admin', 'url': reverse('admin:index')},
    ]

    context = {
        'hour': time_hour_name,
        'dates': many_date,
        'attend': dict_attend,
        'students': full_names,
        'subjects': subjects,
        'teacher': teacher,
        'selected_subject': selected_subject,
        'selected_date': selected_date,
        'submit_teacher': submit_teacher,
        'menu_items': menu_items,
        'success_message': success_message,
    }
    return render(request, 'Attenddef.html', context)


@user_passes_test(lambda u: u.groups.filter(name__in=['HomeroomTeacher', 'SubjectTeacher']).exists(), login_url='')
def Subject_list(request):
    dates = AttendanceInfo.objects.values_list('date', flat=True).distinct()
    department = Department.objects.values_list('name', flat=True).distinct()
    department = list(department)
    hour_instance = Hour.objects.all()
    FirstData = None
    SecondData = None
    ThirdData = None
    ForthData = None
    name = []
    student_data_First_fdata = []
    student_data_First_ldata = []
    student_data_Second_fdata = []
    student_data_Second_ldata = []
    student_data_Third_fdata = []
    student_data_Third_ldata = []
    student_data_Forth_fdata = []
    student_data_Forth_ldata = []
    selected_department = None
    selected_date = None
    max_len = 0
    many_date = [date.strftime("%Y-%m-%d") for date in dates]
    today_date = date.today().strftime("%Y-%m-%d")
    if today_date not in many_date:
        many_date.append(today_date)
    if request.method == "POST":

        if 'department' in request.POST:
            print("POST of department")
            selected_department = request.POST.get('department')
            selected_date = request.POST.get('date')
            print(selected_date)

            if dates:
                last_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
                # 1つ目の日付でフィルタリング
                students = User.objects.filter(
                    groups__name='Student', departments__name=selected_department)
                # 生徒ごとにループ
                for hour in hour_instance:
                    # 各 hour ごとの出席情報を取得
                    attendance_info = AttendanceInfo.objects.filter(
                        date=last_date, time=hour)
                    # 生徒ごとにループ
                    for student in students:
                        student_full_name = student.full_name  # 生徒の氏名を取得
                        if student_full_name not in name:
                            name.append(student_full_name)
                        # 生徒の出席情報が存在する場合、データを更新
                        if attendance_info.filter(student=student).exists():
                            student_attendance = attendance_info.get(
                                student=student)
                            if hour == hour_instance[0]:
                                # print(hour_instance[0])
                                student_data_First_fdata.append(
                                    student_attendance.first_half.type)
                                student_data_First_ldata.append(
                                    student_attendance.latter_half.type)
                                FirstData = student_attendance.subject.subject
                            elif hour == hour_instance[1]:
                                # print(hour_instance[1])
                                # print(student_attendance.first_half.type)
                                student_data_Second_fdata.append(
                                    student_attendance.first_half.type)
                                student_data_Second_ldata.append(
                                    student_attendance.latter_half.type)
                                SecondData = student_attendance.subject.subject
                            elif hour == hour_instance[2]:
                                # print(hour_instance[2])
                                # print(student_attendance.first_half.type)
                                student_data_Third_fdata.append(
                                    student_attendance.first_half.type)
                                student_data_Third_ldata.append(
                                    student_attendance.latter_half.type)
                                ThirdData = student_attendance.subject.subject
                            elif hour == hour_instance[3]:
                                # print(hour_instance[3])
                                # print(student_attendance.first_half.type)
                                student_data_Forth_fdata.append(
                                    student_attendance.first_half.type)
                                student_data_Forth_ldata.append(
                                    student_attendance.latter_half.type)
                                ForthData = student_attendance.subject.subject
                print(student_data_First_fdata)
                print(student_data_First_ldata)
                print(student_data_Second_fdata)
                print(student_data_Second_ldata)
                print(student_data_Third_fdata)
                print(student_data_Third_ldata)
                print(student_data_Forth_fdata)
                print(student_data_Forth_ldata)
                print(name)
            else:
                # 日付が存在しない場合の処理を追加
                attendanceinfo_filtered = None

        if 'button_1' in request.POST:
            print("Button 1 clicked. Redirecting...")
            redirect_url = reverse('ATbook:Attenddef')
            request.session['time'] = hour_instance[0].id
            request.session['selected_date'] = selected_date
            request.session['selected_department'] = selected_department
            request.session['s_subject'] = FirstData
            return HttpResponseRedirect(redirect_url)

        if 'button_2' in request.POST:
            print("Button 2 clicked. Redirecting...")
            redirect_url = reverse('ATbook:Attenddef')
            request.session['time'] = hour_instance[1].id
            request.session['selected_date'] = selected_date
            request.session['selected_department'] = selected_department
            request.session['s_subject'] = SecondData
            return HttpResponseRedirect(redirect_url)

        if 'button_3' in request.POST:
            print("Button 3 clicked. Redirecting...")
            redirect_url = reverse('ATbook:Attenddef')
            request.session['time'] = hour_instance[2].id
            request.session['selected_date'] = selected_date
            request.session['selected_department'] = selected_department
            request.session['s_subject'] = ThirdData
            return HttpResponseRedirect(redirect_url)

        if 'button_4' in request.POST:
            print("Button 4 clicked. Redirecting...")
            redirect_url = reverse('ATbook:Attenddef')
            request.session['time'] = hour_instance[3].id
            request.session['selected_date'] = selected_date
            request.session['selected_department'] = selected_department
            request.session['s_subject'] = ForthData
            return HttpResponseRedirect(redirect_url)

        max_len = max(len(name), len(student_data_First_fdata), len(student_data_First_ldata), len(student_data_Second_fdata), len(
            student_data_Second_ldata), len(student_data_Third_fdata), len(student_data_Third_ldata), len(student_data_Forth_fdata), len(student_data_Forth_ldata))
        print(max_len)
    menu_items = [
        {'name': 'Logout', 'url': reverse('loginapp:logout')},
        {'name': 'Teachers List', 'url': reverse('ATbook:Teacherslist')},
        {'name': 'Attend Definition', 'url': reverse('ATbook:Attenddef')},
        {'name': 'Admin', 'url': reverse('admin:index')},
    ]
    context = {
        "selected_department": selected_department,
        "selected_date": selected_date,
        "dates": many_date,
        "department": department,
        'menu_items': menu_items,
        "student_data": [
            {

                "student": name[i] if i < len(name) else None,
                "First_f": student_data_First_fdata[i] if i < len(student_data_First_fdata) else None,
                "First_l": student_data_First_ldata[i] if i < len(student_data_First_ldata) else None,
                "Second_f": student_data_Second_fdata[i] if i < len(student_data_Second_fdata) else None,
                "Second_l": student_data_Second_ldata[i] if i < len(student_data_Second_ldata) else None,
                "Therd_f": student_data_Third_fdata[i] if i < len(student_data_Third_fdata) else None,
                "Therd_l": student_data_Third_ldata[i] if i < len(student_data_Third_ldata) else None,
                "Forth_f": student_data_Forth_fdata[i] if i < len(student_data_Forth_fdata) else None,
                "Forth_l": student_data_Forth_ldata[i] if i < len(student_data_Forth_ldata) else None,
            }
            for i in range(max_len)
        ]
    }
    return render(request, 'subject_list.html', context)


def Double_slider(request):
    subject_attendance = {}  # 空の辞書を作成
    user = request.user
    attendance_info_list = AttendanceInfo.objects.filter(student=user)

    for attendance_info in attendance_info_list:
        subject = attendance_info.subject.subject  # 科目を取得
        date = attendance_info.date.strftime('%Y-%m-%d')
        print(date)
        # subjectのキーがまだ存在しない場合、新しい辞書を作成
        if subject not in subject_attendance:
            subject_attendance[subject] = {}

        # dateのキーがまだ存在しない場合、新しい辞書を作成
        if date not in subject_attendance[subject]:
            subject_attendance[subject][date] = {
                'first_half': [], 'latter_half': []}

        # first_half と latter_half に出席情報を追加
        subject_attendance[subject][date]['first_half'].append(
            attendance_info.first_half.type)
        subject_attendance[subject][date]['latter_half'].append(
            attendance_info.latter_half.type)

    print(subject_attendance)
    context = {
        'subject_attendance': subject_attendance,
    }
    return render(request, 'double_slider.html', context)
