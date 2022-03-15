from django.db import models

# Create your models here.
# This is role table
class Role(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=50)

    def __str__(self):
        return self.roleName

# This is user table

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20,null=True)

    roleId = models.ForeignKey('adminportal.Role',on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName

#This is your course table
class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseDescription = models.TextField()
    INACTIVE = 0
    ACTIVE = 1
    STATUS =( (INACTIVE, ('INACTIVE')),
             (ACTIVE, ('ACTIVE')),

    )
    active = models.IntegerField(default=0, choices=STATUS)

    class Meta:
        db_table = "Courses"

    def __str__(self):
        return self.courseName
# # This is student course table
class StudentCourse(models.Model):
    studentCourseId = models.AutoField(primary_key=True)
    courseId = models.ForeignKey('adminportal.Course',on_delete=models.CASCADE)

# # This is batch table
class Batch(models.Model):
    batchId = models.AutoField(primary_key=True)
    courseId = models.ForeignKey('adminportal.Course',on_delete=models.CASCADE,blank=True, null=True)
    batchName = models.CharField(max_length=50)
    # facultyId = models.ForeignKey('faculty.Faculty',on_delete=models.CASCADE)
    batchStartDate = models.DateField()
    batchEndDate = models.DateField()

    class Meta:
        db_table = "Batches"

    def __str__(self):
        return self.batchName

# # This is batch details table
class BatchDetails(models.Model):
    batch_detail_id = models.AutoField(primary_key=True)
    batchId = models.OneToOneField(Batch,on_delete=models.CASCADE,blank=True,null=True)
    # studentId = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    class Meta:
        db_table = "Batchdetails"
# # This is batch time table
class BatchTime(models.Model):
    batchTimeId = models.AutoField(primary_key=True)
    batchId = models.ManyToManyField('adminportal.Batch')
    batchDay = models.DateField()
    batchTime = models.TimeField()
    batchDuration = models.DurationField()   

    class Meta:
        db_table = "BatchTimings"
# # This is attendes table
class Attendance(models.Model):
    attendenceId = models.AutoField(primary_key=True)
    batchId = models.ForeignKey('adminportal.Batch', on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = "Attendance"
