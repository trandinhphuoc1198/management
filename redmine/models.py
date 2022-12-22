# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgileColors(models.Model):
    container_type = models.CharField(max_length=255, blank=True, null=True)
    container_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agile_colors'


class AgileData(models.Model):
    issue_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    story_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agile_data'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class Attachments(models.Model):
    container_id = models.IntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=30, blank=True, null=True)
    filename = models.CharField(max_length=255)
    disk_filename = models.CharField(max_length=255)
    filesize = models.BigIntegerField()
    content_type = models.CharField(max_length=255, blank=True, null=True)
    digest = models.CharField(max_length=64)
    downloads = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    disk_directory = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class AuthSources(models.Model):
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    host = models.CharField(max_length=60, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    account_password = models.CharField(max_length=255, blank=True, null=True)
    base_dn = models.CharField(max_length=255, blank=True, null=True)
    attr_login = models.CharField(max_length=30, blank=True, null=True)
    attr_firstname = models.CharField(max_length=30, blank=True, null=True)
    attr_lastname = models.CharField(max_length=30, blank=True, null=True)
    attr_mail = models.CharField(max_length=30, blank=True, null=True)
    onthefly_register = models.IntegerField()
    tls = models.IntegerField()
    filter = models.TextField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    verify_peer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_sources'


class Boards(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    topics_count = models.IntegerField()
    messages_count = models.IntegerField()
    last_message_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boards'


class Changes(models.Model):
    changeset_id = models.IntegerField()
    action = models.CharField(max_length=1)
    path = models.TextField()
    from_path = models.TextField(blank=True, null=True)
    from_revision = models.CharField(max_length=255, blank=True, null=True)
    revision = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changes'


class ChangesetParents(models.Model):
    changeset_id = models.IntegerField()
    parent_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changeset_parents'


class Changesets(models.Model):
    repository_id = models.IntegerField()
    revision = models.CharField(max_length=255)
    committer = models.CharField(max_length=255, blank=True, null=True)
    committed_on = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    commit_date = models.DateField(blank=True, null=True)
    scmid = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changesets'
        unique_together = (('repository_id', 'revision'),)


class ChangesetsIssues(models.Model):
    changeset_id = models.IntegerField()
    issue_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changesets_issues'
        unique_together = (('changeset_id', 'issue_id'),)


class ChecklistTemplateCategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_template_categories'


class ChecklistTemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    template_items = models.TextField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    tracker_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_templates'


class Checklists(models.Model):
    is_done = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=512, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    issue_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_section = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklists'


class Comments(models.Model):
    commented_type = models.CharField(max_length=30)
    commented_id = models.IntegerField()
    author_id = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class CustomFieldEnumerations(models.Model):
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field_enumerations'


class CustomFields(models.Model):
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    field_format = models.CharField(max_length=30)
    possible_values = models.TextField(blank=True, null=True)
    regexp = models.CharField(max_length=255, blank=True, null=True)
    min_length = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    is_required = models.IntegerField()
    is_for_all = models.IntegerField()
    is_filter = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    searchable = models.IntegerField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    editable = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()
    multiple = models.IntegerField(blank=True, null=True)
    format_store = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_fields'


class CustomFieldsProjects(models.Model):
    custom_field_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_projects'
        unique_together = (('custom_field_id', 'project_id'),)


class CustomFieldsRoles(models.Model):
    custom_field_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_roles'
        unique_together = (('custom_field_id', 'role_id'),)


class CustomFieldsTrackers(models.Model):
    custom_field_id = models.IntegerField()
    tracker_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_trackers'
        unique_together = (('custom_field_id', 'tracker_id'),)


class CustomValues(models.Model):
    customized_type = models.CharField(max_length=30)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_values'


class Documents(models.Model):
    project_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class EmailAddresses(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=255)
    is_default = models.IntegerField()
    notify = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_addresses'


class EnabledModules(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'enabled_modules'


class Enumerations(models.Model):
    name = models.CharField(max_length=30)
    position = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    project_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    position_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enumerations'


class GroupsUsers(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups_users'
        unique_together = (('group_id', 'user_id'),)


class ImportItems(models.Model):
    import_id = models.IntegerField()
    position = models.IntegerField()
    obj_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_items'


class Imports(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    filename = models.CharField(max_length=255, blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    total_items = models.IntegerField(blank=True, null=True)
    finished = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'imports'


class IssueCategories(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=60)
    assigned_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_categories'


class IssueRelations(models.Model):
    issue_from_id = models.IntegerField()
    issue_to_id = models.IntegerField()
    relation_type = models.CharField(max_length=255)
    delay = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_relations'
        unique_together = (('issue_from_id', 'issue_to_id'),)


class IssueStatuses(models.Model):
    name = models.CharField(max_length=30)
    is_closed = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_statuses'


class Issues(models.Model):
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    is_private = models.IntegerField()
    closed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class JournalDetails(models.Model):
    journal_id = models.IntegerField()
    property = models.CharField(max_length=30)
    prop_key = models.CharField(max_length=30)
    old_value = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_details'


class Journals(models.Model):
    journalized_id = models.IntegerField()
    journalized_type = models.CharField(max_length=30)
    user_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField()
    private_notes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'journals'


class MemberRoles(models.Model):
    member_id = models.IntegerField()
    role_id = models.IntegerField()
    inherited_from = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_roles'


class Members(models.Model):
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    mail_notification = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'members'
        unique_together = (('user_id', 'project_id'),)


class Messages(models.Model):
    board_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    replies_count = models.IntegerField()
    last_reply_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    locked = models.IntegerField(blank=True, null=True)
    sticky = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class News(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    comments_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class OpenIdAuthenticationAssociations(models.Model):
    issued = models.IntegerField(blank=True, null=True)
    lifetime = models.IntegerField(blank=True, null=True)
    handle = models.CharField(max_length=255, blank=True, null=True)
    assoc_type = models.CharField(max_length=255, blank=True, null=True)
    server_url = models.TextField(blank=True, null=True)
    secret = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_id_authentication_associations'


class OpenIdAuthenticationNonces(models.Model):
    timestamp = models.IntegerField()
    server_url = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'open_id_authentication_nonces'


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    inherit_members = models.IntegerField()
    default_version_id = models.IntegerField(blank=True, null=True)
    default_assigned_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class ProjectsTrackers(models.Model):
    project_id = models.IntegerField()
    tracker_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projects_trackers'
        unique_together = (('project_id', 'tracker_id'),)


class Queries(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    filters = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    column_names = models.TextField(blank=True, null=True)
    sort_criteria = models.TextField(blank=True, null=True)
    group_by = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queries'


class QueriesRoles(models.Model):
    query_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'queries_roles'
        unique_together = (('query_id', 'role_id'),)


class Repositories(models.Model):
    project_id = models.IntegerField()
    url = models.CharField(max_length=255)
    login = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    root_url = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    path_encoding = models.CharField(max_length=64, blank=True, null=True)
    log_encoding = models.CharField(max_length=64, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repositories'


class Roles(models.Model):
    name = models.CharField(max_length=30)
    position = models.IntegerField(blank=True, null=True)
    assignable = models.IntegerField(blank=True, null=True)
    builtin = models.IntegerField()
    permissions = models.TextField(blank=True, null=True)
    issues_visibility = models.CharField(max_length=30)
    users_visibility = models.CharField(max_length=30)
    time_entries_visibility = models.CharField(max_length=30)
    all_roles_managed = models.IntegerField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesManagedRoles(models.Model):
    role_id = models.IntegerField()
    managed_role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles_managed_roles'
        unique_together = (('role_id', 'managed_role_id'),)


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Settings(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Taggings(models.Model):
    tag_id = models.IntegerField(blank=True, null=True)
    taggable_type = models.CharField(max_length=255, blank=True, null=True)
    taggable_id = models.IntegerField(blank=True, null=True)
    tagger_type = models.CharField(max_length=255, blank=True, null=True)
    tagger_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taggings'
        unique_together = (('tag_id', 'taggable_id', 'taggable_type', 'context', 'tagger_id', 'tagger_type'),)


class Tags(models.Model):
    name = models.CharField(unique=True, max_length=255, db_collation='utf8mb3_bin', blank=True, null=True)
    taggings_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TimeEntries(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField(blank=True, null=True)
    hours = models.FloatField()
    comments = models.CharField(max_length=1024, blank=True, null=True)
    activity_id = models.IntegerField()
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'time_entries'


class Tokens(models.Model):
    user_id = models.IntegerField()
    action = models.CharField(max_length=30)
    value = models.CharField(unique=True, max_length=40)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'


class Trackers(models.Model):
    name = models.CharField(max_length=30)
    is_in_chlog = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    is_in_roadmap = models.IntegerField()
    fields_bits = models.IntegerField(blank=True, null=True)
    default_status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trackers'


class UserIssueMonths(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    issue = models.IntegerField(blank=True, null=True)
    odr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_issue_months'


class UserPreferences(models.Model):
    user_id = models.IntegerField()
    others = models.TextField(blank=True, null=True)
    hide_mail = models.IntegerField(blank=True, null=True)
    time_zone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_preferences'


class Users(models.Model):
    login = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=40)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=255)
    admin = models.IntegerField()
    status = models.IntegerField()
    last_login_on = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    auth_source_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    identity_url = models.CharField(max_length=255, blank=True, null=True)
    mail_notification = models.CharField(max_length=255)
    salt = models.CharField(max_length=64, blank=True, null=True)
    must_change_passwd = models.IntegerField()
    passwd_changed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versions(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    wiki_page_title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sharing = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'versions'


class Watchers(models.Model):
    watchable_type = models.CharField(max_length=255)
    watchable_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watchers'


class WikiContentVersions(models.Model):
    wiki_content_id = models.IntegerField()
    page_id = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    compression = models.CharField(max_length=6, blank=True, null=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_content_versions'


class WikiContents(models.Model):
    page_id = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_contents'


class WikiPages(models.Model):
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    protected = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiki_pages'


class WikiRedirects(models.Model):
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    redirects_to = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField()
    redirects_to_wiki_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_redirects'


class Wikis(models.Model):
    project_id = models.IntegerField()
    start_page = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wikis'


class Workflows(models.Model):
    tracker_id = models.IntegerField()
    old_status_id = models.IntegerField()
    new_status_id = models.IntegerField()
    role_id = models.IntegerField()
    assignee = models.IntegerField()
    author = models.IntegerField()
    type = models.CharField(max_length=30, blank=True, null=True)
    field_name = models.CharField(max_length=30, blank=True, null=True)
    rule = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflows'


class WtDailyMemos(models.Model):
    day = models.DateField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wt_daily_memos'


class WtHolidays(models.Model):
    holiday = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wt_holidays'


class WtMemberOrders(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    prj_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wt_member_orders'


class WtProjectOrders(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    dsp_prj = models.IntegerField(blank=True, null=True)
    dsp_pos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wt_project_orders'


class WtTicketRelays(models.Model):
    issue_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wt_ticket_relays'
