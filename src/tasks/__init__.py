"""Tasks module - Contains all crew tasks"""

from .intent_tasks import create_intent_task
from .summary_tasks import create_summary_task
from .compare_tasks import create_compare_task
from .qna_tasks import create_qna_task

__all__ = [
    'create_intent_task',
    'create_summary_task',
    'create_compare_task',
    'create_qna_task'
]
