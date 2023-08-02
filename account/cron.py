from django_cron import CronJobBase, Schedule
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from datetime import datetime


class BlacklistFlush(CronJobBase):
    schedule = Schedule(run_every_mins=0.1, retry_after_failure_mins=5)
    code = 'account.cron.BlacklistFlush'

    def flush(self):
        # BlacklistedToken.objects.filter(token__expires_at__lt=datetime.now()).delete()
        # OutstandingToken.objects.filter(expires_at__lt=datetime.now()).delete()
        print('11111')
