class Image(models.Model):
    """Модель для хранения изображений"""
    public_id = models.UUIDField(db_index=True, unique=True,
                                 default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    total_likes = models.PositiveIntegerField(default=0)
