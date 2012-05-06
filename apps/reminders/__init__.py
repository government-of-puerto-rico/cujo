from __future__ import absolute_import

import datetime

from django.utils.translation import ugettext_lazy as _

from navigation.api import (register_links, register_top_menu,
    register_model_list_columns, register_multi_item_links)
from common.widgets import two_state_template
from common.utils import encapsulate
from acls.api import class_permissions

from .models import Reminder
from .permissions import (PERMISSION_REMINDER_VIEW,
    PERMISSION_REMINDER_CREATE, PERMISSION_REMINDER_EDIT,
    PERMISSION_REMINDER_DELETE)

reminder_list = {'text': _(u'reminder list'), 'view': 'reminder_list', 'famfam': 'hourglass', 'permissions': [PERMISSION_REMINDER_VIEW]}
expired_remider_list = {'text': _(u'expired reminder list'), 'view': 'expired_remider_list', 'famfam': 'tick', 'permissions': [PERMISSION_REMINDER_VIEW]}
reminder_add = {'text': _(u'create reminder (calendar)'), 'view': 'reminder_add', 'famfam': 'hourglass_add', 'permissions': [PERMISSION_REMINDER_CREATE]}
reminder_add_days = {'text': _(u'create reminder (days)'), 'view': 'reminder_add_days', 'famfam': 'hourglass_add', 'permissions': [PERMISSION_REMINDER_CREATE]}
reminder_edit = {'text': _(u'edit (calendar)'), 'view': 'reminder_edit', 'args': 'object.pk', 'famfam': 'hourglass_go', 'permissions': [PERMISSION_REMINDER_EDIT]}
reminder_edit_days = {'text': _(u'edit (days)'), 'view': 'reminder_edit_days', 'args': 'object.pk', 'famfam': 'hourglass_go', 'permissions': [PERMISSION_REMINDER_EDIT]}
future_expired_remider_list = {'text': _(u'future expired reminders'), 'view': 'future_expired_remider_list', 'famfam': 'calendar', 'permissions': [PERMISSION_REMINDER_VIEW]}
reminder_view = {'text': _(u'details'), 'view': 'reminder_view', 'args': 'object.pk', 'famfam': 'hourglass', 'permissions': [PERMISSION_REMINDER_VIEW]}

reminder_delete = {'text': _(u'delete'), 'view': 'reminder_delete', 'args': 'object.id', 'famfam': 'hourglass_delete', 'permissions': [PERMISSION_REMINDER_DELETE]}
reminder_multiple_delete = {'text': _(u'delete'), 'view': 'reminder_multiple_delete', 'famfam': 'hourglass_delete', 'permissions': [PERMISSION_REMINDER_DELETE]}

reminder_group_list_link = {'text': _(u'group list'), 'view': 'reminder_group_list', 'famfam': 'hourglass'}#, 'permissions': [PERMISSION_REMINDER_VIEW]}

register_links(
    [
		'reminder_group_list',
        'comments_for_object', 'comment_add', 'comment_delete', 'comment_multiple_delete',
        'future_expired_remider_list',
        'reminder_view', 'reminder_edit',
        'reminder_edit_days', 'reminder_delete', 'reminder_list',
        'expired_remider_list', 'reminder_add',
        'reminder_add_days', 'participant_add'],
    [
		reminder_group_list_link,
        reminder_list, expired_remider_list,
        future_expired_remider_list,
    ], menu_name='secondary_menu'
)

register_links(
    [
		'reminder_group_list',
        'comments_for_object', 'comment_add', 'comment_delete', 'comment_multiple_delete',
        'future_expired_remider_list',
        'reminder_view', 'reminder_edit',
        'reminder_edit_days', 'reminder_delete', 'reminder_list',
        'expired_remider_list', 'reminder_add',
        'reminder_add_days', 'participant_add'],
    [
        reminder_add, reminder_add_days
    ], menu_name='sidebar'
)

register_links([Reminder],
    [reminder_edit, reminder_edit_days, reminder_delete]
)

register_links([Reminder], [reminder_view], menu_name='form_header')

#register_multi_item_links(
#    [
#        'reminder_list', 'expired_remider_list',
#        'future_expired_remider_list',
#    ],
#    [
#        reminder_multiple_delete
#    ]
#)

register_top_menu('reminders',
    link={'famfam': 'hourglass', 'text': _(u'reminders'), 'view': 'reminder_list'},
    children_path_regex=[r'^reminders', r'comments'], position=1
)

register_model_list_columns(Reminder, [
        {
            'name': _(u'created'),
            'attribute': encapsulate(lambda x: x.datetime_created)
        },
        {
            'name': _(u'expires'),
            'attribute': encapsulate(lambda x: x.datetime_expire)
        },
        {
            'name': _('days'),
            'attribute': encapsulate(lambda x: (x.datetime_expire - x.datetime_created).days)
        },
        {
            'name': _('expired?'),
            'attribute': encapsulate(lambda x: two_state_template((x.datetime_expire < datetime.datetime.now().date()), monostate=True))
        }
    ]
)

class_permissions(Reminder, [
    PERMISSION_REMINDER_VIEW, PERMISSION_REMINDER_CREATE, 
    PERMISSION_REMINDER_EDIT, PERMISSION_REMINDER_DELETE
])
