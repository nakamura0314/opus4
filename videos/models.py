from django.db import models


class Video(models.Model):
    """動画"""

    title = models.CharField('動画タイトル', max_length=255)
    description = models.TextField('説明（空欄可)', blank=True)
    # /media_thumbnails/ファイル名
    # upload_to=はアップロードする場所を示す
    thumbnail = models.ImageField(
        'サムネイル（空欄可)', upload_to='thumbnails/', null=True, blank=True)
    # /media/uploads/2018/3/20/ファイル名
    upload = models.FileField('ファイル', upload_to='uploads/%Y/%m/%d/')
    # default=timezone.nowと違い、入力欄は表示されない、編集ができない
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    # 更新されるたびにその日時が格納される
    # auto_now=Trueとは更新するたびに、ということになる、編集ができない
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title
