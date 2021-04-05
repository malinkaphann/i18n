import i18n

i18n.load_path.append("myapp/locales")
i18n.set('filename_format', '{locale}.{format}')
i18n.set("file_format", 'json')
