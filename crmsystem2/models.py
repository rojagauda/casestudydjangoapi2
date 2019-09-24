from mongoengine import Document, EmbeddedDocument, fields


class Projects(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    name = fields.StringField(
        max_length=255, required=True, null=True)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()
    

class Skills(EmbeddedDocument):
    technology = fields.StringField(max_length=255, required=True, null=False)
    experience = fields.IntField()
    level = fields.StringField(max_length=255, required=False)


class Employee(Document):
    empId = fields.StringField(max_length=10, required=True, null=False)
    empName = fields.StringField(max_length=100, required=True)
    worklocation = fields.StringField(max_length=255, required=False)
    projects = fields.EmbeddedDocumentListField(Projects)
    skills = fields.EmbeddedDocumentListField(Skills)
