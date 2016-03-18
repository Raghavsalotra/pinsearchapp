from django.db import models
from tastypie.utils.timezone import now
from django.db.models.options import Options

class ApiApplications(models.Model):
    owner_type = models.CharField(max_length=10)
    owner_id = models.IntegerField()
    fid = models.IntegerField()
    status = models.IntegerField()
    batch_id = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField()
    call_letter_id = models.IntegerField(blank=True, null=True)
    call_letter_date = models.IntegerField(blank=True, null=True)
    applier_id = models.IntegerField(blank=True, null=True)
    applier_type = models.CharField(max_length=1, blank=True, null=True)
    pm_status = models.IntegerField()
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_applications'
        unique_together = (('owner_type', 'owner_id', 'fid'), ('owner_type', 'owner_id', 'fid'),)


class ApiApplicationsCustom(models.Model):
    fid = models.IntegerField()
    owner_id = models.IntegerField()
    hotjobs_status = models.IntegerField(blank=True, null=True)
    labels = models.TextField(blank=True, null=True)
    admin_comments = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_applications_custom'
        unique_together = (('fid', 'owner_id'),)




class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    state_id = models.IntegerField()
    city_name = models.CharField(max_length=32)
    city_flag = models.IntegerField()
    top_city = models.IntegerField()
    zone_id = models.IntegerField()
    city_rating = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    display_order = models.IntegerField()
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'city'


class ClientType(models.Model):
    client_type_id = models.AutoField(primary_key=True)
    client_type_name = models.CharField(max_length=128)
    client_type_flag = models.IntegerField()
    display_order = models.IntegerField(blank=True, null=True)
    client_type_group = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'client_type'


class ClientUsers(models.Model):
    client_user_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_division_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    personal_email = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    additional_mobile = models.CharField(max_length=10, blank=True, null=True)
    skype_id = models.CharField(max_length=128)
    password = models.CharField(max_length=80, blank=True, null=True)
    activekey = models.CharField(max_length=225, blank=True, null=True)
    contact_person_name = models.CharField(max_length=75, blank=True, null=True)
    contact_person_designation = models.IntegerField(blank=True, null=True)
    std_code = models.CharField(max_length=4, blank=True, null=True)
    contact_no = models.CharField(max_length=16, blank=True, null=True)
    extn = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    address_line2 = models.CharField(max_length=256, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    fw_emp_id = models.IntegerField()
    created_time = models.IntegerField(blank=True, null=True)
    last_updated_time = models.IntegerField(blank=True, null=True)
    last_updated_id = models.IntegerField()
    last_login_time = models.IntegerField(blank=True, null=True)
    email_confirmed = models.IntegerField(blank=True, null=True)
    organic_status = models.IntegerField(blank=True, null=True)
    login_account = models.IntegerField()
    premium_type = models.IntegerField(blank=True, null=True)
    quick_comment = models.TextField(blank=True, null=True)
    delegate_access = models.IntegerField()
    source_id = models.IntegerField(blank=True, null=True)
    src = models.CharField(max_length=256)
    status = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    oldfw_uid = models.IntegerField(blank=True, null=True)
    merge_flag = models.IntegerField()
    delegate_group = models.IntegerField()
    customized_by_fw_emp_id = models.IntegerField(blank=True, null=True)
    old_client_user_id = models.IntegerField(blank=True, null=True)
    last_activity_date = models.IntegerField(blank=True, null=True)
    last_activity_fw_emp_id = models.IntegerField(blank=True, null=True)
    last_activity_id = models.IntegerField(blank=True, null=True)
    microsite_flag = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    mobile_verified = models.IntegerField()
    address_verified = models.IntegerField()
    email_verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_users'


class ContactUs(models.Model):
    name = models.CharField(max_length=500)
    email_id = models.CharField(max_length=500)
    subject = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contact_us'


class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=128)
    corp_flag = models.IntegerField()
    ad_flag = models.IntegerField()
    institute_flag = models.IntegerField()
    designation_flag = models.IntegerField()
    employers_flag = models.CharField(max_length=100)
    manpower_consultants_flag = models.CharField(max_length=100)
    colleges_flag = models.CharField(max_length=100)
    training_institues_flag = models.CharField(max_length=100)
    education_consultants_flag = models.CharField(max_length=100)
    ad_agencies_affiliates_flag = models.CharField(max_length=100)
    others_flag = models.CharField(max_length=100)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designation'





class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class HireBranch(models.Model):
    bid = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)
    branch_short_name = models.CharField(max_length=100)
    cid = models.IntegerField()
    branch_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hire_branch'


class HireCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_type = models.CharField(max_length=100)
    p_flag = models.IntegerField()
    slug = models.CharField(max_length=200, blank=True, null=True)
    branch_map_flag = models.IntegerField()
    institute_map_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hire_course'


class HireDesignation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=128)
    corp_flag = models.IntegerField()
    ad_flag = models.IntegerField()
    institute_flag = models.IntegerField()
    designation_flag = models.IntegerField()
    employers_flag = models.CharField(max_length=100)
    manpower_consultants_flag = models.CharField(max_length=100)
    colleges_flag = models.CharField(max_length=100)
    training_institues_flag = models.CharField(max_length=100)
    education_consultants_flag = models.CharField(max_length=100)
    ad_agencies_affiliates_flag = models.CharField(max_length=100)
    others_flag = models.CharField(max_length=100)
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hire_designation'


class HireJob(models.Model):
    hid = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_profile = models.CharField(max_length=768, blank=True, null=True)
    company_logo_url = models.CharField(max_length=250, blank=True, null=True)
    website_url = models.CharField(max_length=768, blank=True, null=True)
    job_title = models.CharField(max_length=384, blank=True, null=True)
    job_course_id = models.CharField(max_length=50, blank=True, null=True)
    job_branch_id = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    sublocation = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    job_type = models.IntegerField(blank=True, null=True)
    job_type_other = models.CharField(max_length=384, blank=True, null=True)
    date_of_posting = models.IntegerField(blank=True, null=True)
    last_date = models.IntegerField(blank=True, null=True)
    hiring_process = models.CharField(max_length=384, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_twentytwo_words = models.TextField(blank=True, null=True)
    last_date_apply = models.IntegerField(blank=True, null=True)
    rid = models.IntegerField(blank=True, null=True)
    posted_by = models.CharField(max_length=768, blank=True, null=True)
    posted_by_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    creatd_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_job'


class HireJobDesignation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=43)
    role_id = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_job_designation'


class HireJobRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=128)
    role_priority = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_job_role'


class HireMobileVerification(models.Model):
    mobile_no = models.CharField(max_length=15)
    code = models.CharField(max_length=64)
    created_time = models.IntegerField()
    last_updated_time = models.IntegerField()
    status = models.IntegerField()
    comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'hire_mobile_verification'


class HireNotifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=20, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    applier_type = models.CharField(max_length=1, blank=True, null=True)
    push_status = models.IntegerField(blank=True, null=True)
    email_status = models.IntegerField(blank=True, null=True)
    sms_status = models.IntegerField(blank=True, null=True)
    pm_status = models.IntegerField(blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_notifications'


class HireSequnce(models.Model):
    name = models.CharField(max_length=125)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hire_sequnce'


class HireSkills(models.Model):
    skill = models.CharField(max_length=384, blank=True, null=True)
    slug = models.CharField(max_length=1500, blank=True, null=True)
    skill_sub_category = models.IntegerField(blank=True, null=True)
    skill_flag = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_skills'


class HireSublocation(models.Model):
    subloaction_id = models.AutoField(primary_key=True)
    subloaction = models.CharField(max_length=28, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    zone_id = models.IntegerField()
    flag = models.IntegerField(blank=True, null=True)
    display_order = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_sublocation'


class HireUsers(models.Model):
    user_id = models.IntegerField()
    mobile_country_code = models.CharField(max_length=10, blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    email = models.CharField(max_length=75, blank=True, null=True)
    email_phone = models.CharField(max_length=75, blank=True, null=True)
    gcm_regid = models.TextField()
    app_version = models.CharField(max_length=50, blank=True, null=True)
    imei_number = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)
    profile_pic = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    resume_22words = models.TextField(blank=True, null=True)
    full_time_job = models.IntegerField(blank=True, null=True)
    part_time_job = models.IntegerField(blank=True, null=True)
    internship_job = models.IntegerField(blank=True, null=True)
    total_work_exp_inyear = models.CharField(max_length=10, blank=True, null=True)
    total_work_exp_inmonth = models.CharField(max_length=10, blank=True, null=True)
    hq_course_id = models.IntegerField(blank=True, null=True)
    hq_branch_id = models.IntegerField(blank=True, null=True)
    hq_college_id = models.IntegerField(blank=True, null=True)
    hq_aggregate_marks = models.FloatField(blank=True, null=True)
    hq_mark_type = models.CharField(max_length=50, blank=True, null=True)
    hq_year_passout = models.IntegerField(blank=True, null=True)
    current_company = models.CharField(max_length=128, blank=True, null=True)
    current_designation_id = models.IntegerField(blank=True, null=True)
    current_salary = models.IntegerField(blank=True, null=True)
    salary_type = models.CharField(max_length=20, blank=True, null=True)
    current_location = models.CharField(max_length=250, blank=True, null=True)
    current_location_latitude = models.CharField(max_length=100, blank=True, null=True)
    current_location_longitude = models.CharField(max_length=100, blank=True, null=True)
    current_city_id = models.IntegerField(blank=True, null=True)
    current_sublocation_id = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    voice_resume = models.CharField(max_length=100, blank=True, null=True)
    attached_resume = models.CharField(max_length=100, blank=True, null=True)
    profile_completion = models.CharField(max_length=10, blank=True, null=True)
    reg_steps = models.IntegerField(blank=True, null=True)
    resume_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)
    app_updated_time = models.IntegerField(blank=True, null=True)
    resume_updated_time = models.IntegerField(blank=True, null=True)
    last_access_time = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=70, blank=True, null=True)
    src = models.CharField(max_length=200, blank=True, null=True)
    utm_medium = models.CharField(max_length=100, blank=True, null=True)
    utm_content = models.CharField(max_length=100, blank=True, null=True)
    fw_id = models.CharField(max_length=60, blank=True, null=True)
    network_access_point = models.CharField(max_length=25, blank=True, null=True)
    network_operator = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_users'
        unique_together = (('user_id', 'mobile_no'),)


class HireUsersProfileData(models.Model):
    user_id = models.IntegerField()
    profile_pic = models.CharField(max_length=100, blank=True, null=True)
    voice_resume = models.CharField(max_length=100, blank=True, null=True)
    attached_resume = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)
    updated_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hire_users_profile_data'


class HireUsersSkills(models.Model):
    user_id = models.IntegerField()
    skill_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hire_users_skills'


class HotJobProfiles(models.Model):
    fid = models.IntegerField()
    owner_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hot_job_profiles'
        unique_together = (('fid', 'owner_id'),)


class JrResumeSearches(models.Model):
    search_id = models.AutoField(primary_key=True)
    rid = models.IntegerField()
    search_name = models.CharField(max_length=255, blank=True, null=True)
    resume_count = models.IntegerField(blank=True, null=True)
    search_criteria = models.TextField(blank=True, null=True)
    created = models.IntegerField()
    exist_flag = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jr_resume_searches'


class MessageToUser(models.Model):
    client_id = models.CharField(max_length=500)
    user_id = models.CharField(max_length=500)
    message = models.CharField(max_length=500, blank=True, null=True)
    message_type = models.TextField()
    created_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_to_user'


class ResumeUpload(models.Model):
    uid = models.IntegerField()
    resumeupload_path = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'resume_upload'


class Sequences(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sequences'


class Skills(models.Model):
    skill = models.CharField(max_length=128)
    slug = models.CharField(max_length=500)
    skill_sub_category = models.IntegerField()
    skill_flag = models.IntegerField()
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skills'


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    state_flag = models.IntegerField()
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'state'


class UserYii(models.Model):
    username = models.CharField(max_length=255)
    auth_key = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=255)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_yii'


class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    pass_field = models.CharField(db_column='pass', max_length=32)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=64, blank=True, null=True)
    mode = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    theme = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    created = models.IntegerField()
    access = models.IntegerField()
    login = models.IntegerField()
    status = models.IntegerField()
    timezone = models.CharField(max_length=8, blank=True, null=True)
    language = models.CharField(max_length=12, blank=True, null=True)
    picture = models.CharField(max_length=255)
    init = models.CharField(max_length=64, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    encoded_pass = models.CharField(max_length=80)
    dob = models.DateField()
    gender = models.CharField(max_length=8)
    mobile_no = models.CharField(max_length=16)
    std_code = models.CharField(max_length=4)
    contact_no = models.CharField(max_length=16)
    extension = models.CharField(max_length=16)
    address = models.TextField()
    pincode = models.IntegerField()
    city_id = models.IntegerField()
    state_id = models.IntegerField()
    last_update = models.IntegerField()
    email_confirmed = models.IntegerField()
    profile_step_no = models.IntegerField()
    user_type = models.CharField(max_length=1)
    msg_status = models.IntegerField()
    profile_status = models.IntegerField()
    src = models.CharField(max_length=50, blank=True, null=True)
    hq_course_id = models.IntegerField()
    hq_branch_id = models.IntegerField()
    hq_state_id = models.IntegerField()
    hq_institute_id = models.IntegerField()
    hq_university_id = models.IntegerField()
    hq_passout_month = models.IntegerField()
    hq_passout_year = models.IntegerField()
    hq_mark_type = models.CharField(max_length=50)
    hq_aggregate_marks = models.FloatField()
    hq_qualification_type = models.CharField(max_length=50)
    profile_percentage = models.FloatField()
    cron_timestamp = models.IntegerField(blank=True, null=True)
    mobile_country_code = models.CharField(max_length=10, blank=True, null=True)
    mobile_verify = models.IntegerField(blank=True, null=True)
    email_phone = models.CharField(max_length=75, blank=True, null=True)
    gcm_regid = models.TextField(blank=True, null=True)
    app_version = models.CharField(max_length=50, blank=True, null=True)
    imei_number = models.CharField(max_length=25, blank=True, null=True)
    resume_22words = models.TextField(blank=True, null=True)
    full_time = models.IntegerField(blank=True, null=True)
    part_time = models.IntegerField(blank=True, null=True)
    internship = models.IntegerField(blank=True, null=True)
    total_work_exp_inyear = models.CharField(max_length=10, blank=True, null=True)
    total_work_exp_inmonth = models.CharField(max_length=10, blank=True, null=True)
    current_company = models.CharField(max_length=128, blank=True, null=True)
    current_designation_id = models.IntegerField(blank=True, null=True)
    current_salary = models.IntegerField(blank=True, null=True)
    salary_type = models.CharField(max_length=20, blank=True, null=True)
    current_location = models.CharField(max_length=250, blank=True, null=True)
    current_location_latitude = models.CharField(max_length=100, blank=True, null=True)
    current_location_longitude = models.CharField(max_length=100, blank=True, null=True)
    current_city_id = models.IntegerField(blank=True, null=True)
    current_sublocation_id = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    voice_resume = models.CharField(max_length=100, blank=True, null=True)
    attached_resume = models.CharField(max_length=100, blank=True, null=True)
    app_reg_steps = models.IntegerField(blank=True, null=True)
    app_resume_status = models.IntegerField(blank=True, null=True)
    app_created_time = models.IntegerField(blank=True, null=True)
    app_updated_time = models.IntegerField(blank=True, null=True)
    resume_updated_time = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=70, blank=True, null=True)
    utm_medium = models.CharField(max_length=100, blank=True, null=True)
    utm_content = models.CharField(max_length=100, blank=True, null=True)
    network_access_point = models.CharField(max_length=25, blank=True, null=True)
    network_operator = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
