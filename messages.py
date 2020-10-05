from config import (
	tariff_ref_period, tariff_ref_no_subscription_period,
	tariff_ref_notifies, tariff_ref_sub_period)

def get_language(lang_code):
	# Иногда language_code может быть None
	if not lang_code:
		return "en"
	if "-" in lang_code:
		lang_code = lang_code.split("-")[0]
	if lang_code == "ru":
		return "ru"
	elif lang_code == "pt":
		return "pt-BR"  # Бразильский вариант португальского языка
	elif lang_code == "es":
		return "es"
	elif lang_code == "de":
		return "de"
	elif lang_code == "he":
		return "he"
	else:
		return "en"

def get_message(message, lang_code, param=""):
	lang_code = get_language(lang_code)
	if param == "":
		param = "ro_msg"
	try:
		try:
			return messages.get(message).get(get_language(lang_code)).get(param)
		except Exception:
			return messages.get(message).get(get_language(lang_code)).get("ro_msg")
	except Exception:
		try:
			return messages.get(message).get("en").get("ro_msg")
		except Exception:
			return " "


emojiCodes = {
	'magnifier': '\U0001F50D',
	'microphone': '\U0001F3A4',
	'information': '\U00002139',
	'crown': '\U0001F451',
	'inboxTray': '\U0001F4E5',
	'soundEnabled': '\U0001F514',
	'soundDisabled': '\U0001F515',
	'creditCard': '\U0001F4B3',
	'dollar': '\U0001F4B2',
	'dollarBag': '\U0001F4B0',
	'moneyWithWings': '\U0001F4B8',
	'clipboard': '\U0001F4CB',
	'bronze': '\U0001F949',
	'silver': '\U0001F948',
	'gold': '\U0001F947',
	'gear': '\U00002699'
}


messages = {
	"welcomeMessage": {
		"ru": {
			"ro_msg": "*Добро пожаловать!*\n"
			"Вы можете начать с этих популярных каналов:"
		},
		"en": {
			"ro_msg": "*Welcome!*\n"
			"You can start with these popular channels:"
		},
		"pt-BR": {
			"ro_msg": "*Olá!*\n"
			"Que tal começar com estes podcasts populares?"
		},
		"es": {
			"ro_msg": "*Bienvenido!*\n"
			"Usted puede comenzar con estos canales populares"
		},
		"de": {
			"ro_msg": "*Herzlich Willkommen!*\n"
			"Du kannst mit einem dieser beliebten Podcasts beginnen:"
		},
		"he": {
			"ro_msg": "*ברוכים הבאים!*\n"
			"אתם יכולים להרשם לערוצים הפופולריים הללו:"
		}
	},
	"welcome": {
		"ru": {
			"ro_msg": "*Добро пожаловать!*"
		},
		"en": {
			"ro_msg": "*Welcome!*"
		},
		"pt-BR": {
			"ro_msg": "*Olá!*"
		},
		"es": {
			"ro_msg": "*Bienvenido!*"
		},
		"de": {
			"ro_msg": "*Herzlich Willkommen!*"
		},
		"he": {
			"ro_msg": "ברוכים הבאים!"
		}

	},
	"offerMessage": {
		"ru": {
			"ro_msg": emojiCodes.get('crown') + "\n" + "Популярные каналы:"
		},
		"en": {
			"ro_msg": emojiCodes.get('crown') + "\n" + "Popular channels:"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('crown') + "\n" + "Podcastas populares:"
		},
		"es": {
			"ro_msg": emojiCodes.get('crown') + "\n" + "Canales populares:"
		},
		"de": {
			"ro_msg": emojiCodes.get('crown') + "\n" + "Beliebte Podcasts:"
		},
		"he": {
			"ro_msg": emojiCodes.get('crown') + "\n" + "ערוצים פופולריים:"
		}

	},
	"pressMe": {
		"ru": {
			"ro_msg": "Нажми на меня"
		},
		"en": {
			"ro_msg": "Press me"
		},
		"pt-BR": {
			"ro_msg": "Toque aqui"
		},
		"es": {
			"ro_msg": "Toque aqui"
		},
		"de": {
			"ro_msg": "Drück mich!"
		},
		"he": {
			"ro_msg": "לחצו כאן"
		}
	},
	"subscribe": {
		"ru": {
			"ro_msg": "Подписаться"
		},
		"en": {
			"ro_msg": "Subscribe"
		},
		"pt-BR": {
			"ro_msg": "Assinar"
		},
		"es": {
			"ro_msg": "Suscribirse"
		},
		"de": {
			"ro_msg": "Abonnieren"
		},
		"he": {
			"ro_msg": "הרשמו כמנוי"
		}
	},
	"unsubscribe": {
		"ru": {
			"ro_msg": "Отписаться"
		},
		"en": {
			"ro_msg": "Unsubscribe"
		},
		"pt-BR": {
			"ro_msg": "Desinscrever"
		},
		"es": {
			"ro_msg": "Desuscribirse"
		},
		"de": {
			"ro_msg": "Abo beenden"
		},
		"he": {
			"ro_msg": "ביטול הרשמה כמנוי"
		}

	},
	"notifyon": {
		"ru": {
			# "ro_msg": "Присылать новые эпизоды"
			"ro_msg": "Новые эпизоды " + emojiCodes.get('soundDisabled')
		},
		"en": {
			# "ro_msg": "Send new episodes"
			"ro_msg": "New episodes " + emojiCodes.get('soundDisabled')
		},
		"pt-BR": {
			# "ro_msg": "Enviar novos episódios"
			"ro_msg": "Novos episódios " + emojiCodes.get('soundDisabled')
		},
		"es": {
			"ro_msg": "Nuevos episodios " + emojiCodes.get('soundDisabled')
			# "ro_msg": "Enviar episodios nuevos"
		},
		"de": {
			"ro_msg": "Neue Folgen " + emojiCodes.get('soundDisabled')
			# "ro_msg": "Neue Folgen empfangen"
		},
		"he": {
			# "ro_msg": "Send new episodes"
			"ro_msg": "פרקים חדשים " + emojiCodes.get('soundDisabled')
		}

	},
	"notifyoff": {
		"ru": {
			# "ro_msg": "Не присылать новые эпизоды"
			"ro_msg": "Новые эпизоды " + emojiCodes.get('soundEnabled')
		},
		"en": {
			# "ro_msg": "Do not send new episodes"
			"ro_msg": "New episodes " + emojiCodes.get('soundEnabled')
		},
		"pt-BR": {
			# "ro_msg": "Não enviar novos episódios"
			"ro_msg": "Novos episódios " + emojiCodes.get('soundEnabled')
		},
		"es": {
			"ro_msg": "Nuevos episodios " + emojiCodes.get('soundEnabled')
			# "ro_msg": "No enviar nuevos episodios"
		},
		"de": {
			"ro_msg": "Neue Folgen " + emojiCodes.get('soundEnabled')
			# "ro_msg": "Keine neuen Folgen empfangen"
		},
		"he": {
			# "ro_msg": "Do not send new episodes"
			"ro_msg": "פרקים חדשים " + emojiCodes.get('soundEnabled')
		}

	},
	"notifyoned": {
		"ru": {
			"ro_msg": "Теперь вы будете получать новые эпизоды этого канала!"
		},
		"en": {
			"ro_msg": "You will now receive new episodes from this channel!"
		},
		"pt-BR": {
			"ro_msg": "Agora você irá receber novos episódios deste podcast!"
		},
		"es": {
			"ro_msg": "Ahora usted recibirá nuevos episodios de este canal!"
		},
		"de": {
			"ro_msg": "In Zukunft werden wir Dir neue Folgen dieses Podcasts zusenden."
		},
		"he": {
			"ro_msg": "כעת תקבלו פרקים חדשים מערוץ זה!"
		}

	},
	"notifyoffed": {
		"ru": {
			"ro_msg": "Вы больше не будете получать новые эпизоды этого канала!"
		},
		"en": {
			"ro_msg": "You will no longer receive new episodes from this channel!"
		},
		"pt-BR": {
			"ro_msg": "Você não irá receber mais novos episódios deste podcast!"
		},
		"es": {
			"ro_msg": "Usted ya no recibirá nuevos episodios de este canal!"
		},
		"de": {
			"ro_msg": "Du wirst keine neuen Folgen dieses Podcasts mehr erhalten."
		},
		"he": {
			"ro_msg": "לא תקבלו פרקים חדשים מערוץ זה!"
		}

	},
	"yousubscribedto": {
		"ru": {
			"ro_msg": "Вы подписались на %s"
		},
		"en": {
			"ro_msg": "You subscribed to %s"
		},
		"pt-BR": {
			"ro_msg": "Vocẽ assinou %s"
		},
		"es": {
			"ro_msg": "Usted se suscribió a %s"
		},
		"de": {
			"ro_msg": "Du hast %s abonniert."
			# "ro_msg": "Du hast abonniert:"
			# "ideally": "Du hast %s abonniert."
		},
		"he": {
			"ro_msg": "נרשמתם לערוץ %s"
		}
	},
	"youunsubscribedto": {
		"ru": {
			"ro_msg": "Вы отписались от %s"
		},
		"en": {
			"ro_msg": "You unsubscribed from %s"
		},
		"pt-BR": {
			"ro_msg": "Você cancelou a assinatura de %s"
		},
		"es": {
			"ro_msg": "Usted se desuscribió de %s"
		},
		"de": {
			"ro_msg": "Du hast Dein Abo für %s beendet."
		},
		"he": {
			"ro_msg": "ביטלתם את הרישום מערוץ %s"
		}

	},
	"listen": {
		"ru": {
			"ro_msg": "Слушать"
		},
		"en": {
			"ro_msg": "Listen"
		},
		"pt-BR": {
			"ro_msg": "Ouvir"
		},
		"es": {
			"ro_msg": "Escuchar"
		},
		"de": {
			"ro_msg": "Anhören"
		},
		"he": {
			"ro_msg": "האזן"
		}

	},
	"goBack": {
		"ru": {
			"ro_msg": "❮❮ Назад"
		},
		"en": {
			"ro_msg": "❮❮ Go back"
		},
		"pt-BR": {
			"ro_msg": "❮❮ Voltar"
		},
		"es": {
			"ro_msg": "❮❮ Regresar"
		},
		"de": {
			"ro_msg": "❮❮ Zurück"
		},
		"he": {
			"ro_msg": "❮❮ חזור"
		}

	},
	"goBackMenu": {
		"ru": {
			"ro_msg": "❮❮ Назад в меню"
		},
		"en": {
			"ro_msg": "❮❮ Go back to menu"
		},
		"pt-BR": {
			"ro_msg": "❮❮ Voltar ao menu"
		},
		"es": {
			"ro_msg": "❮❮ Regresar al menú"
		},
		"de": {
			# "ro_msg": "❮❮ Zurück zum Hauptmenü"
			"ro_msg": "❮❮ Hauptmenü"
		},
		"he": {
			"ro_msg": "❮❮ חזור לתפריט"
		}

	},
	"skip": {
		"ru": {
			"ro_msg": "Пропустить"
		},
		"en": {
			"ro_msg": "Skip"
		},
		"pt-BR": {
			"ro_msg": "Pular"
		},
		"es": {
			"ro_msg": "Saltar"
		},
		"de": {
			"ro_msg": "Überspringen"
		},
		"he": {
			"ro_msg": "דלג"
		}

	},
	"backToCHannel": {
		"ru": {
			"ro_msg": "Вернуться к каналу"
		},
		"en": {
			"ro_msg": "Go back to channel"
		},
		"pt-BR": {
			"ro_msg": "Voltar ao canal"
		},
		"es": {
			"ro_msg": "Regresar al canal"
		},
		"de": {
			"ro_msg": "Zurück zur Übersicht"
		},
		"he": {
			"ro_msg": "חזור לערוץ"
		}

	},
	"thereis": {
		"ru": {
			"ro_msg": "Всего"
		},
		"en": {
			"ro_msg": "There are"
		},
		"pt-BR": {
			"ro_msg": "Encontrados"
		},
		"es": {
			"ro_msg": "Se encontraron"
		},
		"de": {
			"ro_msg": "Es gibt"
		},
		"he": {
			"ro_msg": "קיים"
		}

	},
	"records": {
		"ru": {
			"ro_msg": "Записей",
			"1": "Запись",
			"2": "Записи"
		},
		"en": {
			"ro_msg": "Episodes"
		},
		"pt-BR": {
			"ro_msg": "Registros"
		},
		"es": {
			"ro_msg": "Registros"
		},
		"de": {
			"ro_msg": "Folgen",
		},
		"he": {
			"ro_msg": "רשומות"
		}

	},
	"page": {
		"ru": {
			"ro_msg": "Страница"
		},
		"en": {
			"ro_msg": "Page"
		},
		"pt-BR": {
			"ro_msg": "Página"
		},
		"es": {
			"ro_msg": "Página"
		},
		"de": {
			"ro_msg": "Seite"
		},
		"he": {
			"ro_msg": "עמוד"
		}

	},
	"of": {
		"ru": {
			"ro_msg": "Из"
		},
		"en": {
			"ro_msg": "Of"
		},
		"pt-BR": {
			"ro_msg": "De"
		},
		"es": {
			"ro_msg": "De"
		},
		"de": {
			"ro_msg": "Von"
		},
		"he": {
			"ro_msg": "של"
		}

	},
	"alreadyOnThisPage": {
		"ru": {
			"ro_msg": "Вы уже на этой странице"
		},
		"en": {
			"ro_msg": "You are already on this page"
		},
		"pt-BR": {
			"ro_msg": "Você já está nessa página"
		},
		"es": {
			"ro_msg": "Ya usted está en esta página"
		},
		"de": {
			"ro_msg": "Du befindest Dich bereits auf dieser Seite."
		},
		"he": {
			"ro_msg": "אתה כבר בעמוד זה"
		}

	},
	"pageDoesnotExist": {
		"ru": {
			"ro_msg": "Запрашиваемой страницы не существует"
		},
		"en": {
			"ro_msg": "Requested page doesn’t exist"
		},
		"pt-BR": {
			"ro_msg": "A página solicitada não existe"
		},
		"es": {
			"ro_msg": "La página solicitada no existe"
		},
		"de": {
			"ro_msg": "Die angefragte Seite gibt es nicht."
		},
		"he": {
			"ro_msg": "העמוד המבוקש איננו קיים"
		}

	},
	"original": {
		"ru": {
			"ro_msg": "Оригинальный"
		},
		"en": {
			"ro_msg": "Original"
		},
		"pt-BR": {
			"ro_msg": "Original"
		},
		"es": {
			"ro_msg": "Original"
		},
		"de": {
			"ro_msg": "Original"
		},
		"he": {
			"ro_msg": "מְקוֹרִי"
		}
	},
	"error": {
		"ru": {
			"ro_msg": "Ошибка! Попробуйте позже или свяжитесь с разработчиком"
		},
		"en": {
			"ro_msg": "Error! Try again later or contact the developer"
		},
		"de": {
			"ro_msg": "Ein Fehler ist aufgetreten! Versuche es später erneut oder "
			"setze Dich mit dem Entwickler in Verbindung!"
		}
	},
	"parsingError": {
		"ru": {
			"ro_msg": "Ошибка в получении информации о подкасте."
		},
		"en": {
			"ro_msg": "Sorry, an error occured when receiving podcast info."
		},
		"pt-BR": {
			"ro_msg": "Desculpe. Encontramos erro no recebimento das"
			" informações do podcast."
		},
		"es": {
			"ro_msg": "Lo sentinos, ocurrieron errores al recibir la"
			" información del podcast."
		},
		"de": {
			"ro_msg": "Fehler beim Abrufen der Podcast-Informationen."
			" Bitte entschuldige!"
		},
		"he": {
			"ro_msg": "מצטערים, אירעו שגיאות בקבלת המידע על הפודקאסט."
		}

	},
	"gettingStateError": {
		"ru": {
			"ro_msg": "Ошибка в получении вашего состояния, сброс..."
		},
		"en": {
			"ro_msg": "Error in getting your status, resetting..."
		},
		"pt-BR": {
			"ro_msg": "Erro ao obter seu status, redefinir..."
		},
		"es": {
			"ro_msg": "Error al obtener su estado, restableciendo..."
		},
		"de": {
			"ro_msg": "Fehler beim Abrufen Deines Statusses,"
			" Vorgang wird rückabgewickelt…"
		},
		"he": {
			"ro_msg": "אירעה שגיאה בקבלת הסטטוס שלך, מאפס..."
		}
	},
	"somethingWentWrong": {
		"ru": {
			"ro_msg": "Что-то пошло не так, попытайтесь позже"
		},
		"en": {
			"ro_msg": "Something went wrong, try again later"
		},
		"pt-BR": {
			"ro_msg": "Ocorreu um erro. Tente novamente mais tarde"
		},
		"es": {
			"ro_msg": "Algo salió mal, intente nuevamente más tarde"
		},
		"de": {
			"ro_msg": "Es ist ein Fehler aufgetreten. Versuche es später erneut!"
		},
		"he": {
			"ro_msg": "משהו השתבש, נסה שוב מאוחר יותר"
		}
	},
	"needTimeToLoad": {
		"ru": {
			"ro_msg": "Для загрузки необходимо время"
		},
		"en": {
			"ro_msg": "Your download will take some time"
		},
		"pt-BR": {
			"ro_msg": "O download demora um pouco"
		},
		"es": {
			"ro_msg": "La descarga puede demorar un poco"
		},
		"de": {
			"ro_msg": "Das Herunterladen wird einige Zeit in Anspruch nehmen."
		},
		"he": {
			"ro_msg": "לוקח זמן להוריד"
		}

	},
	"tooBigRecord": {
		"ru": {
			"ro_msg": "К сожалению, объём файла подкаста слишком большой для серверов"
			" Telegram. Однако, вы можете прослушать [по ссылке]"
		},
		"en": {
			"ro_msg": "Unfortunately, the podcast file too big for Telegram servers."
			" But you still can listen to it [via link]"
		},
		"pt-BR": {
			"ro_msg": "Infelizmente, o arquivo do podcast é muito grande para os"
			" servidores do Telegram. Você ainda poderá ouvir através deste [link]"
		},
		"es": {
			"ro_msg": "Lamentablemente el tamaño del podcast es demasiado grande para"
			" los servidores de Telegram. Usted puede escucharlo [via link]"
		},
		"de": {
			"ro_msg": "Leider ist die Datei der Folge zu groß für die Telegram-Server."
			" Du kannst sie aber [über den Link] anhören"
		},
		"he": {
			"ro_msg": "לצערינו, גודל הפודקאסט מידי גדול בשביל שרתי טלגרם."
			" אבל אתם עדיין יכולים להאזין לו [ע''י קישור]"
		}

	},
	"tooBigRecord2": {
		"ru": {
			"ro_msg": "В [itunes]"
		},
		"en": {
			"ro_msg": "In [itunes]"
		},
		"pt-BR": {
			"ro_msg": "No [itunes]"
		},
		"es": {
			"ro_msg": "En [itunes]"
		},
		"de": {
			"ro_msg": "Bei [iTunes]"
		},
		"he": {
			"ro_msg": "ב[itunes]"
		}

	},
	"tooBigRecord3": {
		"ru": {
			"ro_msg": "Или на [сайте подкаста]"
		},
		"en": {
			"ro_msg": "Or on [the podcast web site]"
		},
		"pt-BR": {
			"ro_msg": "Ou no [site do podcast]"
		},
		"es": {
			"ro_msg": "O en el [sitio web del podcast]"
		},
		"de": {
			"ro_msg": "Oder auf [der Webseite des Podcasts]"
		},
		"he": {
			"ro_msg": "או ב[אתר הפודקאסט]"
		}

	},
	"recordUnavaliable": {
		"ru": {
			"ro_msg": "К сожалению, файл подкаста недоступен."
			" Попробуйте открыть его на [официальном сайте]("
		},
		"en": {
			"ro_msg": "Unfortunately, the podcast file is unavaliable."
			" Try to open it’s [official site]("
		},
		"pt-BR": {
			"ro_msg": "Infelizmente, o arquivo do podcast não está disponível."
			" Tente abrir o [site oficial]("
		},
		"es": {
			"ro_msg": "Lamentablemente el fichero del podcast no está disponoble."
			" Intenta abrir su [sitio oficial]("
		},
		"de": {
			"ro_msg": "Leider ist die Datei der Episode nicht verfügbar."
			" Versuche es auf der [offiziellen Webseite]("
		},
		"he": {
			"ro_msg": "לצערינו, קובץ הפודקאסט לא ניתן לבחירה."
			" נסה לפתוח את [האתר הרשמי]("
		}
	},
	"recordUnavaliable2": {
		"ru": {
			"ro_msg": "Или по [прямой ссылке на файл]("
		},
		"en": {
			"ro_msg": "Or by [direct link to the file]("
		},
		"pt-BR": {
			"ro_msg": "Ou pelo [link direto para o arquivo]("
		},
		"es": {
			"ro_msg": "O por [enlace directo al archivo]("
		},
		"de": {
			"ro_msg": "Oder mit dem [Link zur Datei]("
		},
		"he": {
			"ro_msg": "או ע''י [קישור ישיר לקובץ]("
		}
	},
	"search": {
		"ru": {
			"ro_msg": emojiCodes.get('magnifier') + " " + "Поиск"
		},
		"en": {
			"ro_msg": emojiCodes.get('magnifier') + " " + "Search"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('magnifier') + " " + "Pesquisar"
		},
		"es": {
			"ro_msg": emojiCodes.get('magnifier') + " " + "Buscar"
		},
		"de": {
			"ro_msg": emojiCodes.get('magnifier') + " " + "Suche"
		},
		"he": {
			"ro_msg": emojiCodes.get('magnifier') + " " + "חפש"
		}

	},
	"subscriptions": {
		"ru": {
			"ro_msg": emojiCodes.get('microphone') + " " + "Подписки"
		},
		"en": {
			"ro_msg": emojiCodes.get('microphone') + " " + "Subscriptions"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('microphone') + " " + "Assinaturas"
		},
		"es": {
			"ro_msg": emojiCodes.get('microphone') + " " + "Suscripciones"
		},
		"de": {
			"ro_msg": emojiCodes.get('microphone') + " " + "Abos"
		},
		"he": {
			"ro_msg": emojiCodes.get('microphone') + " " + "מינויים"
		}

	},
	"update": {
		"ru": {
			"ro_msg": emojiCodes.get('inboxTray') + " " + "Обновить"
		},
		"en": {
			"ro_msg": emojiCodes.get('inboxTray') + " " + "Refresh"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('inboxTray') + " " + "Atualizar"
		},
		"es": {
			"ro_msg": emojiCodes.get('inboxTray') + " " + "Actualizar"
		},
		"de": {
			"ro_msg": emojiCodes.get('inboxTray') + " " + "Aktualisieren"
		},
		"he": {
			"ro_msg": emojiCodes.get('inboxTray') + " " + "עדכון"
		}
	},
	"lastUpdate": {
		"ru": {
			"ro_msg": "Обновлено"
		},
		"en": {
			"ro_msg": "Updated"
		},
		"pt-BR": {
			"ro_msg": "Atualizar"
		},
		"es": {
			"ro_msg": "Actualizado"
		},
		"de": {
			"ro_msg": "Stand"
		},
		"he": {
			"ro_msg": "מעודכן"
		}

	},
	"uploaded": {
		"ru": {
			"ro_msg": "Загружено"
		},
		"en": {
			"ro_msg": "Uploaded"
		},
		"pt-BR": {
			"ro_msg": "Carregado"
		},
		"es": {
			"ro_msg": "Subido"
		},
		"de": {
			"ro_msg": "Hochgeladen"
		},
		"he": {
			"ro_msg": "הועלה"
		}

	},
	"settings": {
		"ru": {
			"ro_msg": emojiCodes.get('gear') + " Настройки"
		},
		"en": {
			"ro_msg": emojiCodes.get('gear') + " Settings"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('gear') + " Configurações"
		},
		"es": {
			"ro_msg": emojiCodes.get('gear') + " Configuración"
		},
		"de": {
			"ro_msg": emojiCodes.get('gear') + " Einstellungen"
		},
		"he": {
			"ro_msg": emojiCodes.get('gear') + "הגדרות"
		}

	},
	"bot_settings": {
		"ru": {
			"ro_msg": emojiCodes.get('gear') + "Глобальные настройки бота"
		},
		"en": {
			"ro_msg": emojiCodes.get('gear') + "Global bot settings"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('gear') + "Configurações globais de bot"
		},
		"es": {
			"ro_msg": emojiCodes.get('gear') + "Configuración global de bot"
		},
		"de": {
			"ro_msg": emojiCodes.get('gear') + "Globale Bot-Einstellungen"
		},
		"he": {
			"ro_msg": emojiCodes.get('gear') + "הגדרות בוט גלובליות"
		}
	},
	"bitrate": {
		"ru": {
			"ro_msg": "Битрейт"
		},
		"en": {
			"ro_msg": "Bitrate"
		},
		"pt-BR": {
			"ro_msg": "Taxa de bits"
		},
		"es": {
			"ro_msg": "Bitrate"
		},
		"de": {
			"ro_msg": "Bitrate"
		},
		"he": {
			"ro_msg": "קצב סיביות"
		}
	},
	"bitrate_settings_description": {
		"ru": {
			"ro_msg":
				emojiCodes.get('gear') + " *Выберите битрейт*\n\n"
				"Например, если битрейт составляет"
				" 64 kbit/s, то запись длиной 10 минут будет занимать около 4.6 мегабайт."
				"\nВ то же время, если битрейт будет в 2 раза больше, то и размер файла"
				" увеличится в 2 раза.\nДанный параметр влияет на качество записи.\n\n"
				"Текущий битрейт: "
		},
		"en": {
			"ro_msg": emojiCodes.get('gear') + " *Select bitrate *\n\n"
			"For example, if the bitrate is"
			" 64 kbit/s, then a 10 minute recording will take about 4.6 megabytes."
			"\nAt the same time, if the bitrate is 2 times higher, then the file size"
			" will double.\nThis parameter affects the recording quality.\n\n"
			"Current bitrate:"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('gear') + "*Selecione taxa de bits*\n\n"
			"Por exemplo, se a taxa de bits for"
			" 64 kbit/s, uma gravação de 10 minutos levará cerca de 4,6 megabytes."
			"\nAo mesmo tempo, se a taxa de bits for 2 vezes maior, o tamanho do"
			" arquivo dobrará.\nEste parâmetro afeta a qualidade da gravação.\n\n"
			"Taxa de bits atual:"
		},
		"es": {
			"ro_msg": emojiCodes.get('gear') + "*Seleccionar bitrate*\n\n"
			"Por ejemplo, si la tasa de bits es"
			" 64 kbit/s, luego una grabación de 10 minutos tomará alrededor de 4,6 "
			"megabytes.\nl mismo tiempo, si la tasa de bits es 2 veces mayor, entonces"
			"el tamaño del archivo se duplicará.\nEste parámetro afecta la calidad de "
			"grabación.\n\nVelocidad de bits actual:"
		},
		"de": {
			"ro_msg": emojiCodes.get('gear') + "*Bitrate auswählen*\n\n"
			"Wenn die Bitrate beispielsweise"
			" 64 kbit/s beträgt, dann belegt eine 10-minütige Aufnahme etwa 4,6 Megabyte."
			"\nAnalog verdoppelt sich bei doppelter Bitrate auch die "
			"Dateigröße.\nDieser Parameter wirkt sich auf die "
			"Aufnahmequalität aus.\n\nAktuelle Bitrate:"
		}
	},
	"do_not_change_bitrate": {
		"ru": {
			"ro_msg": "Не изменять битрейт"
		},
		"en": {
			"ro_msg": "Don't change bitrate"
		},
		"pt-BR": {
			"ro_msg": "Não mude a taxa de bits"
		},
		"es": {
			"ro_msg": "No cambie la tasa de bits"
		},
		"de": {
			"ro_msg": "Bitrate nicht ändern"
		}
	},
	"bitrate_changed": {
		"ru": {
			"ro_msg": "Битрейт изменён, новое значение: "
		},
		"en": {
			"ro_msg": "Bitrate changed, new value: "
		},
		"pt-BR": {
			"ro_msg": "Taxa de bits alterada, novo valor: "
		},
		"es": {
			"ro_msg": "Bitrate cambiado, nuevo valor: "
		},
		"de": {
			"ro_msg": "Bitrate geändert, neuer Wert: "
		}
	},
	"podcastOffer": {
		"ru": {
			"ro_msg": emojiCodes.get('crown') + " " + "Интересные подкасты"
		},
		"en": {
			"ro_msg": emojiCodes.get('crown') + " " + "Recommendations"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('crown') + " " + "Sugestões"
		},
		"es": {
			"ro_msg": emojiCodes.get('crown') + " " + "Le puede gustar"
		},
		"de": {
			"ro_msg": emojiCodes.get('crown') + " " + "Empfehlungen"
		},
		"he": {
			"ro_msg": emojiCodes.get('crown') + " " + "אולי תאהב את זה"
		}

	},
	"help": {
		"ru": {
			"ro_msg": emojiCodes.get('information') + " " + "Помощь"
		},
		"en": {
			"ro_msg": emojiCodes.get('information') + " " + "Help"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('information') + " " + "Ajuda"
		},
		"es": {
			"ro_msg": emojiCodes.get('information') + " " + "Ayuda"
		},
		"de": {
			"ro_msg": emojiCodes.get('information') + " " + "Hilfe"
		},
		"he": {
			"ro_msg": emojiCodes.get('information') + " " + "עזרה"
		}

	},
	"menuMessage": {
		"ru": {
			"ro_msg": "Выберите действие из предложенных:"
		},
		"en": {
			"ro_msg": "Please choose what you want to do:"
		},
		"pt-BR": {
			"ro_msg": "Por favor, escolha uma das opções a seguir:"
		},
		"es": {
			"ro_msg": "Por favor, seleccione lo que quiere hacer:"
		},
		"de": {
			"ro_msg": "Bitte wähle eine der folgenden Möglichkeiten:"
		},
		"he": {
			"ro_msg": "אנא בחר מה שברצונך לעשות:"
		}

	},
	"searchAdv": {
		"ru": {
			"ro_msg": (
				emojiCodes.get('magnifier') + "\n"
				+ "Пришлите мне название подкаста, который вы хотите найти."
				" Например, 'Лайфхакер'")
		},
		"en": {
			"ro_msg": (
				emojiCodes.get('magnifier') + "\n"
				+ "Send me the name of a podcast you want to find."
				" For example, 'Off The Vine with Kaitlyn Bristowe'")
		},
		"pt-BR": {
			"ro_msg": (
				emojiCodes.get('magnifier') + "\n"
				+ "Envie o o nome do podcast que você deseja pesquisar."
				" Por exemplo, 'Café Brasil'")
		},
		"es": {
			"ro_msg": (
				emojiCodes.get('magnifier') + "\n"
				+ "Envíe el nombre del podcast que quiere encontrar."
				" Por ejemplo, 'El enjambre'")
		},
		"de": {
			"ro_msg": (
				emojiCodes.get('magnifier') + "\n"
				+ "Schicke mir den Namen eines Podcasts, den Du finden möchtest,"
				" zum Beispiel „Whocast”.")
		},
		"he": {
			"ro_msg": (
				emojiCodes.get('magnifier') + "\n"
				+ "שלח לי את שם הפודקאסט שברצונך למצוא."
				" לדוגמא, 'הפודיום'")
		}

	},
	"cancel": {
		"ru": {
			"ro_msg": "Отмена"
		},
		"en": {
			"ro_msg": "Cancel"
		},
		"pt-BR": {
			"ro_msg": "Cancelar"
		},
		"es": {
			"ro_msg": "Cancelar"
		},
		"de": {
			"ro_msg": "Abbrechen"
		},
		"he": {
			"ro_msg": "ביטול"
		}
	},
	"searchResults": {
		"ru": {
			"ro_msg": "Результаты поиска:"
		},
		"en": {
			"ro_msg": "Search results:"
		},
		"pt-BR": {
			"ro_msg": "Resultados:"
		},
		"es": {
			"ro_msg": "Resultados:"
		},
		"de": {
			"ro_msg": "Suchergebnisse:"
		},
		"he": {
			"ro_msg": "תוצאות חיפוש:"
		}

	},
	"loading": {
		"ru": {
			"ro_msg": "Загрузка... Пожалуйста, подождите!"
		},
		"en": {
			"ro_msg": "Loading... Please, wait for a while!"
		},
		"pt-BR": {
			"ro_msg": "Carregando... Por favor, aguarde!"
		},
		"es": {
			"ro_msg": "Cargando... Por favor, espere!"
		},
		"de": {
			"ro_msg": "Wird geladen… Bitte warte einen Moment!"
		},
		"he": {
			"ro_msg": "טוען... אנא המתן!"
		}
	},
	"donate": {
		"ru": {
			"ro_msg": "Помочь боту"
		},
		"en": {
			"ro_msg": "Support this bot"
		},
		"pt-BR": {
			"ro_msg": "Colabore com o bot"
		},
		"es": {
			"ro_msg": "Colabore con este bot"
		},
		"de": {
			"ro_msg": "Spenden"
		},
		"he": {
			"ro_msg": "רובוט עזרה"
		}
	},
	"subsMessage": {
		"ru": {
			"ro_msg": (
				emojiCodes.get('microphone') + "\n"
				+ "Список подкастов, на которые вы подписаны:")
		},
		"en": {
			"ro_msg": (
				emojiCodes.get('microphone') + "\n"
				+ "List of podcasts to which you are subscribed:")
		},
		"pt-BR": {
			"ro_msg": (
				emojiCodes.get('microphone') + "\n"
				+ "Podcasts que você assinou:")
		},
		"es": {
			"ro_msg": (
				emojiCodes.get('microphone') + "\n"
				+ "Lista de Podcasts a los que se ha suscrito:")
		},
		"de": {
			"ro_msg": (
				emojiCodes.get('microphone') + "\n"
				+ "Liste deiner Podcast-Abonnements:")
		},
		"he": {
			"ro_msg": (
				emojiCodes.get('microphone') + "\n"
				+ "רשימת הפודקאסטים אליהם נרשמת:")
		}
	},
	"noNewRecords": {
		"ru": {
			"ro_msg": "Новых эпизодов нет!"
		},
		"en": {
			"ro_msg": "No new episodes!"
		},
		"pt-BR": {
			"ro_msg": "Nenhum episódio novo!"
		},
		"es": {
			"ro_msg": "No hay episodios nuevos!"
		},
		"de": {
			"ro_msg": "Keine neuen Folgen."
		},
		"he": {
			"ro_msg": "אין פרקים חדשים!"
		}
	},
	"noSubs": {
		"ru": {
			"ro_msg": "У вас нет подписок."
		},
		"en": {
			"ro_msg": "You have no subscriptions!"
		},
		"pt-BR": {
			"ro_msg": "Você não tem inscrições!"
		},
		"es": {
			"ro_msg": "Usted no tiene suscripciones!"
		},
		"de": {
			"ro_msg": "Du hast nichts abonniert."
		},
		"he": {
			"ro_msg": "אין לך מינויים!"
		}
	},
	"podcastDoesNotExist": {
		"ru": {
			"ro_msg": "Не удалось получить данные подкаста, попробуйте позже."
			" Возможно, он был удалён или автор не разрешает просматривать его.\n"
			"Внимание, если вы подписаны и отпишетесь сейчас, то вы, возможно,"
			" больше не сможете подписаться."
		},
		"en": {
			"ro_msg": "Failed to get podcast data, try again later."
			" It may have been deleted or the author does not allow viewing it.\n"
			"Attention, if you are subscribed and unsubscribe now,"
			" then you may no longer be able to subscribe."
		},
		"pt-BR": {
			"ro_msg": "Falha ao obter dados do podcast, tente depois."
			" Talvez tenha sido removido pelo autor ou o autor não permite a sua"
			" visualização.\nAtenção! Se você estiver inscrito e cancelar sua"
			" assinatura, talvez você não consiga mais se inscrever."
		},
		"es": {
			"ro_msg": "Error al obtener datos de podcast, intente nuevamente."
			" Tal vez haya sido eliminado o el autor no permite la visualización.\n"
			"Atención! Si está suscrito y cancelado su suscripción,"
			" es posible que no pueda volver a suscribirse."
		},
		"de": {
			"ro_msg": "Abrufen der Podcast-Daten fehlgeschlagen. Versuche es später"
			" erneut. Womöglich wurde er gelöscht oder der Besitzer verbietet den"
			" Zugriff.\n"
			"Vorsicht! Falls Du diesen Podcast abonniert hast und nun Dein Abo"
			" beendest,"
			" ist es Dir eventuell nicht mehr möglich, ihn erneut zu abonnieren."
		},
		"he": {
			"ro_msg": "השגת נתוני הפודקאסט נכשלה. נסה מאוחר יותר."
			" יתכן שהוא נמחק או שהמחבר אינו מאפשר להציג אותו.\n"
			"שים לב, אם אתה רשום ותבטל כעת את המינוי,"
			" יתכן שלא תוכל לחזור ולהרשם."
		}
	},
	"botDescr": {
		"ru": {
			"ro_msg": "Этот бот позволяет вам искать, слушать и подписываться"
			" на подкасты. Если вы подпишитесь на какой-нибудь канал,"
			" то при выходе нового выпуска бот пришлёт его вам."
		},
		"en": {
			"ro_msg": "This bot allows you to search, listen and subscribe to podcasts."
			" If you subscribe to any channel, then when a new release appears,"
			" the bot will send it to you."
		},
		"pt-BR": {
			"ro_msg": "Este bot permite pesquisar, escutar e assinar podcasts."
			" Se você assinar um podcast,"
			" o bot irá enviar novos episódios assim que forem lançado."
		},
		"es": {
			"ro_msg": "Este bot le permite buscar, escuchar y suscribirse a podcasts."
			" Si usted se suscribe a algún canal,"
			" cuando haya nuevos episodios el bot se los enviará."
		},
		"de": {
			"ro_msg": "Dieser Bot ermöglicht es Dir, Podcasts zu suchen,"
			" sie anzuhören und zu abonnieren."
			" Nachdem Du einen Podcast abonniert hast,"
			" wird der Bot dir neue Episoden schicken wann immer sie herauskommen."
		},
		"he": {
			"ro_msg": "בוט זה מאפשר לך לחפש, להאזין ולהירשם לפודקאסטים."
			" אם אתה נרשם לערוץ מסוים, כשיופיע פרק חדש,"
			" הבוט ישלח לך אותו."
		}
	},
	"whatPodcastIs": {
		"ru": {
			"ro_msg": "Подкастинг (англ. podcasting, от iPod и англ. broadcasting"
			" — повсеместное вещание, широковещание) — процесс создания"
			" и распространения звуковых или видеофайлов (подкастов) в стиле"
			" радио- и телепередач в Интернете (вещание в Интернете)."
			" Как правило, подкасты имеют определённую тематику и периодичность издания"
			" (определение Евгения Мятина)."
		},
		"en": {
			"ro_msg": "Podcasting (from iPod and broadcasting)"
			" is the process of creating and distributing"
			" audio or video files (podcasts) in the style of radio and television"
			" broadcasts on the Internet (broadcasting on the Internet). As a rule,"
			" podcasts have a certain theme and frequency of publication (this"
			" definition was given by Evgeny Myatin)."
		},
		"pt-BR": {
			"ro_msg": "O podcast (de iPod e broadcast) é o processo de criação e"
			" distribuição de arquivos de áudio ou vídeo (os podcasts) no estilo de"
			" transmissões de rádio e televisão na Internet. Como regra, os podcasts"
			" têm um certo tema e frequência de publicação (essa definição foi dada"
			" por Evgeny Myatin)."
		},
		"es": {
			"ro_msg": "Podcast (de iPod y broadcast) es el proceso de crear y"
			" distribuir archivos de audio o video (podcasts) como si fueran"
			" transmisiones de radio o televisión a través de internet. Como regla"
			" general, los podcasts tienen una cierta temática y frecuencia en sus"
			" publicaciones (esta definición fue dada por Evgeny Myatin)."
		},
		"de": {
			"ro_msg": "Podcasten (engl. podcasting, von iPod und engl. broadcasting"
			" – allgemeiner Rundfunk, Sendung) beschreibt das Erstellen und Verteilen"
			" von Ton- und Bilddateien (Podcasts) über das Internet, welche Radio-"
			" und Fernsehsendungen ähneln. In der Regel haben Podcasts feste"
			" Form und Veröffentlichungstermine."
			" (Diese Definition stammt von Evgeny Myatin.)"
		},
		"he": {
			"ro_msg": "פודקאסטים (מה iPod או מהסטרימינג) הם תוכנית שמע או ווידאו"
			" שמשודרים על ידי האינטרנט באמצעות פודקאסט"
			" בעברית פודקאסט היו 'הסכת'."
			" הפודקאסט הינו מקביל לתוכנית רדיו או טלוויזיה, אך משודר באינטרנט."
			" לפודקאסטים יש לרוב פרקי זמן קבועים של הפצה."
			" (הסבר זה נכתב  ע''י יבגני מייטין ותורגם ע''י מקליד תמיד)."
		}
	},
	"functsDescr": {
		"ru": {
			"ro_msg": "Чтобы найти новые подкасты, перейдите в /menu и нажмите на"
			" поиск. Затем отправьте боту название или часть названия подкаста,"
			" который вы хотите найти. Во многих списках, в том числе и поиске,"
			" работает постраничная навигация.\n\n"
			"Чтобы подписаться на подкаст, нажмите \"Подписаться\", открыв интересующий"
			" канал. Чтобы прослушать его подкасты, нажмите \"Cлушать\". Если, открыв"
			" записи подкаста по нажатию на кнопку \"Слушать\" и ввести число, то"
			" откроется эта страница.\n\n"
			"Если из /menu нажать на \"Подписки\", то вы сможете посмотреть на список"
			" своих подписок. Здесь также можно ввести число и сразу перейти на данную"
			" страницу.\n\n"
			"Бот высылает новые выпуски автоматически, однако вы можете проверить"
			" наличие новых записей вручную, нажав на \"Обновить\" в /menu. Кнопка "
			"\"Интересные подкасты\" предложит вам познакомиться с новыми каналами.\n\n"
			"Кроме всего этого бот поддерживает несколько команд, которые начинаются с"
			" /, например /menu. Чтобы посмотреть их полный список, введите / в чате."
		},
		"en": {
			"ro_msg": "To find new podcasts, go to /menu and click on search."
			" Then send the bot the name or part of the name of the podcast you want"
			" to find. Paging navigation works in many lists, including search.\n\n"
			"To subscribe to a podcast, click \"Subscribe\" to open the channel of"
			" interest. To listen to its podcasts, click \"Listen\". If you open a"
			" podcast’s recordings by pressing the \"Listen\""
			" button and enter a number,"
			" this page will open.\n\n"
			"By clicking on \"Subscriptions\" from /menu, you can look at the"
			" list of your subscriptions. Here you can also enter a number and go"
			" directly to the corresponding page.\n\n"
			"The bot sends new episodes automatically, but you can check for new"
			" entries manually by clicking on \"Update\" in /menu."
			" The \"Recommendations\" button will invite you to get acquainted with new"
			" channels.\n\n"
			"Besides all this, the bot supports several commands that start with /,"
			" for example /menu. To view the full list of commands,"
			" enter / in the chat."
		},
		"pt-BR": {
			"ro_msg": "Para encontrar novos podcasts, vá em /menu e toque em pesquisar."
			" Em seguida, envie ao bot o nome ou parte do nome do podcast que você"
			" deseja encontrar. A navegação por páginas funciona em várias listas,"
			" incluindo os resultados da pesquisa.\n\n"
			"Para assinar um podcast, toque em \"Assinar\" para abrir o podcasts"
			" escolhido. Para ouvir seus podcasts, toque em \"Ouvir\". Você pode"
			" navegar na lista de episódios, ou digitar diretamente o número da"
			" página.\n\n"
			"Se você tocar em \"Assinaturas\", poderá ver a lista de seus podcasts."
			" Nesta lista também é possível inserir um número e ir diretamente para"
			" uma página.\n\n"
			"O bot envia novos episódios automaticamente, mas você pode procurar por"
			" novos manualmente tocando em \"Atualizar\". O botão \"Sugestões\" irá"
			" sugerir alguns podcastas interessantes para começar.\n\n"
			"Além disso, o bot suporta vários comandos que começam com /. Por exemplo"
			" /menu. Para consultar a lista completa, digite / no chat..."
		},
		"es": {
			"ro_msg": "Para encontrar nuevos podcasts, diríjase a /menu y presione"
			" buscar. Luego envíe al bot el nombre del podcast que quiere encontrar."
			" La navegación por páginas funciona en varias listas, incluyendo la"
			" búsqueda.\n\n"
			"Para suscribirse a un podcast, seleccione \"Suscribirse\" para abrir el"
			" canal seleccionado. Para escuchar sus podcasts, seleccione \"Escuchar\"."
			" Si usted abre un podcast presionando el botón \"Escuchar\" y entra un"
			" número, esta página se abrirá.\n\n"
			"Si usted selecciona \"Suscripciones\" desde /menu, entonces usted podrá"
			" ver su lista de suscripciones. Aquí también podrá entrar un número e ir"
			" directamente a la página.\n\n"
			"El bot envía episodios nuevos automáticamente, pero usted puede chequear"
			" manualmente presionando \"Actualizar\"en /menu. El botón"
			" \"Podcasts interesantes\" lo invitará a seguir nuevos canales.\n\n"
		},
		"de": {
			"ro_msg": "Um neue Podcasts zu finden, gehe ins Hauptmenü und wähle die"
			" Suche. Sende dann den Namen des gesuchten Podcasts oder einen Teil"
			" des Namens als Nachricht. Viele Listen werden auf Seiten aufgeteilt"
			" angezeigt, darunter auch die Suchergebnisse.\n\n"
			"Um einen Podcast zu abonnieren, wähle „Abonnieren“. Auf das"
			" Folgen-Archiv kannst Du über „Anhören“ zugreifen. Wählst Du „Anhören“"
			" und schickst anschließend eine"
			" Zahl als Nachricht, wechselt die Ansicht zur entsprechenden Seite.\n\n"
			"Wählst Du „Abos“ im Hauptmenü (Befehl /menu) siehst Du die Liste Deiner"
			" Abonnements. Auch hier kannst Du durch Eingabe einer Zahl direkt zu"
			" einer bestimmten Seite springen.\n\n"
			"Der Bot verschickt neue Folgen automatisch, aber Du kannst auch von Hand"
			" überprüfen, ob neue Einträge verfügbar sind, indem Du im /menu "
			"„Aktualisieren” wählst. Der „Empfehlungen”-Button lädt Dich ein, neue"
			" Podcasts kennenzulernen.\n\n"
			"Darüber hinaus bietet der Bot eine Reihe an Befehlen, welche alle mit"
			" / beginnen, /menu beispielsweise. Gib / ins Nachrichtenfeld ein, um eine"
			" vollständige Liste zu sehen."
		},
		"he": {
			"ro_msg": "כדי למצוא פודקאסטים חדשים כנסו ל /menu ולחצו על חיפוש,"
			" ושלחו לרובוט את שם הפודקאסט הרצוי או חלק ממנו "
			" כדי למצוא. ניווט בהחלפה פועל בהרבה רשימות כולל בחיפוש.\n\n"
			"כדי להרשם לפודקאסט לחץ \"Subscribe\" כדי לפתוח את הערוץ של"
			" הפודקאסט. כדי להאזין לפודקאסטים שלו לחצו על \"Listen\". אם אתה פותח"
			" הקלטות פודקאסט על ידי לחיצה על כפתור \"Listen\" והזינו את מספר"
			" הדף שהנכם מעוניינים לפתוח.\n\n"
			"אם תלחצו על \"Subscriptions\" מתוך /menu, תוכלו לראות את"
			" רשימת המנויים שלכם. כאן תוכלו גם להזין מספר וללכת"
			" ישירות לעמוד זה.\n\n"
			"הבוט שולח פרקים חדשים אוטומטית, אך אתה יכול לבדוק אם הם חדשים"
			" על ידי כניסה ידנית עם לחיצה על \"Update\" ב /menu. כפתור ה \"Interesting"
			" podcasts\" יזמין אותך להתוודע לחדשים"
			" בערוצים.\n\n"
			"חוץ מזה, הרובוט תומך במספר פקודות שמתחילות ב /,"
			" לדוגמה /menu. לצפיה ברשימת הפקודות המלאה, שלח / בצ'אט."
		}
	},
	"yes": {
		"ru": {
			"ro_msg": "Да"
		},
		"en": {"ro_msg": "Yes"},
		"de": {"ro_msg": "Ja"}
	},
	"no": {
		"ru": {
			"ro_msg": "Нет"
		},
		"en": {"ro_msg": "No"},
		"de": {"ro_msg": "Nein"}
	},
	"unlimited": {
		"ru": {
			"ro_msg": "Неограниченно"
		},
		"en": {"ro_msg": "Unlimited"},
		"de": {"ro_msg": "Unbegrenzt"}
	},
	"disable": {
		"ru": {
			"ro_msg": "Отключить"
		},
		"en": {
			"ro_msg": "Disable"
		},
		"de": {
			"ro_msg": "Deaktivieren"
		}
	},
	"not_selected": {
		"ru": {
			"ro_msg": "Не выбран"
		},
		"en": {
			"ro_msg": "Not selected"
		},
		"de": {
			"ro_msg": "Nicht ausgewählt"
		}
	},
	"youAlreadySubscribedOnTariff": {
		"ru": {
			"ro_msg": "Вы уже подписаны на данный тариф"
		},
		"en": {
			"ro_msg": "You are already subscribed to this tariff"
		},
		"de": {
			"ro_msg": "Du bist bereits in dieser Preisklasse."
		}
	},
	"tariffActivatedNotEnoughMoney": {
		"ru": {
			"ro_msg": "Вы уже подписаны на данный тариф, но он не активирован.\n"
			"Чтобы активировать его, вам надо положить на баланс ещё %s" + \
			emojiCodes.get('dollar') + "(доллары)."
		},
		"en": {
			"ro_msg": "You have already subscribed to this tariff, but it has not"
			" been activated. \nTo activate it, you need to add %s to your balance" + \
			emojiCodes.get('dollar') + "(dollars)."
		},
		"de": {
			"ro_msg": "Du bist bereits in dieser Preisklasse, sie wurde aber noch nicht"
			" aktiviert. \nUm sie zu aktivieren musst Du Deinen Kontostand um %s erhöhen" + \
			emojiCodes.get('dollar') + "(in Dollar)."
		}
	},
	"notEnoughMoneyToActivate": {
		"ru": {
			"ro_msg": "Недостаточно средств чтобы активировать тариф.\n"
			"Чтобы активировать его до конца текущего срока, вам надо положить на "
			"баланс ещё %s" + emojiCodes.get('dollar') + "(доллары)."
		},
		"en": {
			"ro_msg": "Insufficient funds to activate the tariff.\n"
			"To fully activate it, you need to add %s to your balance" + \
			emojiCodes.get('dollar') + "(dollars)."
		},
		"de": {
			"ro_msg": "Deine Mittel sind unzureichend, um diese Preisklasse freizuschalten.\n"
			"Um sie vollständig zu aktivieren musst Du Deinen Kontostand um %s erhöhen" + \
			emojiCodes.get('dollar') + "(in Dollar)."
		}
	},
	"tariffSuccessChanged": {
		"ru": {
			"ro_msg": "Тариф успешно применён!"
		},
		"en": {
			"ro_msg": "The tariff has been successfully applied!"
		},
		"de": {
			"ro_msg": "Deine Preisklasse wurde erfolgreich angepasst!"
		}
	},
	"tariffNotActive": {
		"ru": {
			"ro_msg": "Тариф не активирован! Чтобы активировать его, пополните баланс"
		},
		"en": {
			"ro_msg": "The tariff is not activated! To activate it, top up your balance"
		},
		"de": {
			"ro_msg": "Die Preisklasse ist nicht aktiv! Lade zum Freischalten Dein Konto auf!"
		}
	},
	"bot_subscription": {
		"ru": {
			"ro_msg": emojiCodes.get('creditCard') + " " + "Подписка"
		},
		"en": {
			"ro_msg": emojiCodes.get('creditCard') + " " + "Subscription"
		},
		"de": {
			"ro_msg": emojiCodes.get('creditCard') + " " + "Aufstocken"
		}
	},
	"bot_sub_page_header": {
		"ru": {
			"ro_msg": emojiCodes.get('creditCard') + " Подписка на бота"
		},
		"en": {
			"ro_msg": emojiCodes.get('creditCard') + " Bot subscription"
		},
		"de": {
			"ro_msg": emojiCodes.get('creditCard') + " Bot-Abonnement"
		}
	},
	"donate_page_body": {
		"ru": {
			"ro_msg": "Подписка позволяет получить доступ ко всем возможностям бота.\n"
			"Существует несколько тарифов. Чтобы узнать подробнее и подписаться, "
			"нажмите на кнопку \"Выбрать тариф\".\nЧтобы внести деньги на счёт,"
			" нажмите на кноку \"Пополнить баланс\"."
		},
		"en": {
			"ro_msg": "Subscription allows you to access all the features of the bot.\n"
			"There are several tariffs. To learn more and subscribe,"
			"click on the \"Choose a tariff\" button.\nTo deposit money into your "
			"account, click on the \"Top up balance\" button."
		},
		"de": {
			"ro_msg": "Im Abonnement erhälst Du Zugriff auf alle Funktionen des Bots.\n"
			"Es gibt mehrere Preisklassen. Um mehr zu erfahren und um zu abonnieren, "
			"drücke „Preisklasse wählen”!\nUm Dein Konto aufzuladen, "
			"drücke „Konto aufladen”!"
		}
	},
	"donate_page_referal": {
		"ru": {
			"ro_msg": "Приводите друзей и получайте бонусы! Если по вашей ссылке "
			"перейдёт человек, то вы получите дополнительные " + str(
				int(tariff_ref_period / 24)) + " дней и " + str(tariff_ref_notifies) \
			+ " уведомлений к текущему тарифу или, если вы не подписаны, " \
			+ str(int(tariff_ref_no_subscription_period / 24)) + " дня подписки на "
			"минимальный тариф. Если по вашей ссылке пополнят баланс, то ваш тариф"
			" будет изменён на максимальный, а его срок увеличится на " + str(int(
				tariff_ref_sub_period / 24)) + " дней."
		},
		"en": {
			"ro_msg": "Bring friends and get bonuses! If a person follows your link"
			", you will get additional" + str(
				int(tariff_ref_period / 24)) + " days and " + str(tariff_ref_notifies) \
			+ " notifications to the current tariff or, if you are not subscribed," \
			+ str(int(tariff_ref_no_subscription_period / 24)) + " days of subscription"
			" for minimum tariff. If a person refills the balance using your link, then"
			" your tariff will be changed to the maximum, and its term will increase "
			"by " + str(int(tariff_ref_sub_period / 24)) + " days."
		},
		"de": {
			"ro_msg": "Werbe Freunde und erhalte Prämien! Folgt jemand Deinem Link"
			", erhältst Du " + str(
				int(tariff_ref_period / 24)) + " zusätzliche Tage und " + str(tariff_ref_notifies) \
			+ " zusätzliche Benachrichtigungen in Deiner aktuellen Preisklasse. Falls Du kein Abonnement besitzt," \
			" erhältst Du " + str(int(tariff_ref_no_subscription_period / 24)) + " Abonnement-Tage"
			" in der niedrigsten Preisklasse. Wenn jemand über Deinen Link seinen Kontostand auflädt,"
			" wechselst Du in die höchste Preisklasse und Dein Abonnement wird "
			"um " + str(int(tariff_ref_sub_period / 24)) + " Tage verlängert."
		}
	},
	"curr_tariff": {
		"ru": {
			"ro_msg": "Текущий тариф"
		},
		"en": {
			"ro_msg": "Current tariff"
		},
		"de": {
			"ro_msg": "Aktuelle Preisklasse"
		}
	},
	"you_cant_recieve_notifications": {
		"ru": {
			"ro_msg": "С текущими условиями вам не будут приходить уведомления о новых "
			"выпусках.\nПодробнее: /subscription"
		},
		"en": {
			"ro_msg": "With the current conditions, you will not receive notifications "
			"about new releases.\nMore details: /subscription"
		},
		"de": {
			"ro_msg": "Unter den aktuellen Bedingungen wirst Du keine Benachrichtigungen "
			"bei neuen Folgen erhalten.\nWeitere Informationen unter /subscription"
		}
	},
	"tariffs": {
		"ru": {
			"ro_msg": emojiCodes.get('clipboard') + " Выбрать тариф"
		},
		"en": {
			"ro_msg": emojiCodes.get('clipboard') + "Choose a tariff"
		},
		"de": {
			"ro_msg": emojiCodes.get('clipboard') + "Preisklasse wählen"
		}
	},
	"bot_sub_trfs_page": {
		"ru": {
			"ro_msg": "*" + emojiCodes.get('clipboard') + " Тарифы*\n\n"
			"Здесь вы можете выбрать подходящий тариф. Внимательно ознакомьтесь"
			" с доступными вариантами, а затем нажмите на кнопку нужного тарифа\n\n"
			"Тариф не активируется, пока вы не пополните ваш счёт."
			"*Внимание! Пополнение счёта также считается безвозмездным пожертвованием!*"
			"\n\nЕсли вы решите перейти на более дорогой тариф, то сразу же спишется "
			"часть разницы между тарифами за оставшиеся дни\n*Но если решите перейти "
			"на более дешёвый, то баланс увеличится на половину стоимости за оставшиеся"
			" дни, кроме текущего!*"
		},
		"en": {
			"ro_msg": "*" + emojiCodes.get('clipboard') + " Tariffs*\n\n"
			"Here you can choose a suitable tariff. Please read carefully"
			" with available options, and then click on the button for the desired "
			"tariff\n\nThe tariff is not activated until you fund your account."
			"*Attention! Account funding is also considered a donation!*"
			"\n\nIf you decide to switch to a more expensive tariff, then part of the "
			"difference between the tariffs for the remaining days will be debited "
			"immediately\n*But if you decide to switch to a cheaper one, the balance "
			"will increase by half the cost for the remaining days, except for the "
			"current one!*"
		},
		"de": {
			"ro_msg": "*" + emojiCodes.get('clipboard') + " Preisklassen*\n\n"
			"Hier kannst Du eine für Dich passende Preisklasse wählen. Lies Dir "
			"die verfügbaren Optionen aufmerksam durch! Dann drücke auf die gewünschte "
			"Preisklasse!\n\nDein Abonnement wird nicht freigeschaltet, bis Du Deinen "
			"Kontostand auflädst. *Beachte: Deinen Kontostand aufzuladen wird auch als "
			"Spende gesehen!*"
			"\n\nWenn Du Dich entscheidest, in eine teurere Preisklasse zu wechseln, wird "
			"ein Teil der Preisdifferenz für die verbleibende Laufzeit des Abonnements sofort "
			"abgebucht.\n*Wenn Du aber entscheidest in eine günstigere Preisklasse zu "
			"wechseln, wird Dein Kontostand um die Hälfte der Kosten für die verbleibende "
			"Laufzeit erhöht, ausgenommen dem Tag des Wechsels selbst!*"
		}
	},
	"tariff_lvl1": {
		"ru": {
			"ro_msg": emojiCodes.get('bronze') + " Бронза"
		},
		"en": {
			"ro_msg": emojiCodes.get('bronze') + " Bronze"
		},
		"de": {
			"ro_msg": emojiCodes.get('bronze') + " Bronze"
		}
	},
	"tariff_lvl2": {
		"ru": {
			"ro_msg": emojiCodes.get('silver') + " Серебро"
		},
		"en": {
			"ro_msg": emojiCodes.get('silver') + " Silver"
		},
		"de": {
			"ro_msg": emojiCodes.get('silver') + " Silber"
		}
	},
	"tariff_lvl3": {
		"ru": {
			"ro_msg": emojiCodes.get('gold') + " Золото"
		},
		"en": {
			"ro_msg": emojiCodes.get('gold') + " Gold"
		},
		"de": {
			"ro_msg": emojiCodes.get('gold') + " Gold"
		}
	},
	"trf_descr_tmplt": {
		"ru": {
			"ro_msg": "Стоимость: %s" + emojiCodes.get('dollar') \
			+ "(долларов) за 30 дней.\nУведомлений (за период, 30 дней): %s\n"
			# "Поддержка сжатия: (недоступно на данный момент) %s"
		},
		"en": {
			"ro_msg": "Cost: %s" + emojiCodes.get('dollar') \
			+ "(dollars) for 30 days.\nNotifications (for a period of 30 days): %s\n"
			# "Compression support: (not available at the moment) %s"
		},
		"de": {
			"ro_msg": "Kosten: %s" + emojiCodes.get('dollar') \
			+ "(in Dollar) für 30 Tage.\nBenachrichtigungen (über eine Laufzeit von 30 Tagen): %s\n"
			# "Compression support: (not available at the moment) %s"
		}
	},
	"days_left": {
		"ru": {
			"ro_msg": "Осталось дней: %s"
		},
		"en": {
			"ro_msg": "Days left: %s"
		},
		"de": {
			"ro_msg": "Verbleibende Tage: %s"
		}
	},
	"notify_left": {
		"ru": {
			"ro_msg": "Осталось уведомлений: %s"
		},
		"en": {
			"ro_msg": "Notifications left: %s"
		},
		"de": {
			"ro_msg": "Verbleibende Benachrichtigungen: %s"
		}
	},
	"curr_balance": {
		"ru": {
			"ro_msg": "Текущий баланс: %s" + emojiCodes.get('dollar')
		},
		"en": {
			"ro_msg": "Current balance: %s" + emojiCodes.get('dollar')
		},
		"de": {
			"ro_msg": "Kontostand: %s" + emojiCodes.get('dollar')
		}
	},
	"not_enough_for_renewal": {
		"ru": {
			"ro_msg": "(не хватает для продления: %s" + emojiCodes.get('dollar') + ")"
		},
		"en": {
			"ro_msg": "(not enough for renewal: %s" + emojiCodes.get('dollar') + ")"
		},
		"de": {
			"ro_msg": "(nicht genug für eine Erneuerung: %s" + emojiCodes.get('dollar') + ")"
		}
	},
	"topUpBalance": {
		"ru": {
			"ro_msg": emojiCodes.get('moneyWithWings') + " Пополнить баланс"
		},
		"en": {
			"ro_msg": emojiCodes.get('moneyWithWings') + " Top up balance"
		},
		"de": {
			"ro_msg": emojiCodes.get('moneyWithWings') + " Konto aufladen"
		}
	},
	"bot_sub_pmnt_page": {
		"ru": {
			"ro_msg": "*" + emojiCodes.get('moneyWithWings') + " Пополнение*\n\n"
			"Здесь вы можете пополнить баланс. Для получения ссылки можно нажать"
			" на кнопку или *ввести сумму вручную*.\n\n"
			"*Внимание! Пополнение счёта также считается безвозмездным пожертвованием!*"
			" Доллары в системе — это виртуальные очки, выдающиеся за пожертвования"
			", при этом они принадлежат владельцем бота, а не пользователям. "
			"Администрация и владелец бота не несут ответственность за пожертвованные "
			"деньги, баланс в системе и виртуальные очки. Выбранный пользователем тариф"
			" может быть отменён, а баланс аннулирован в любое время без объяснения "
			"причин.\nВ то же время администрация будет идти на контакт и разрешать "
			"споры по возможности и в зависимости от ситуации."
		},
		"en": {
			"ro_msg": "*" + emojiCodes.get('moneyWithWings') + " Deposit*\n\n"
			"Here you can top up your balance. For a link you can click"
			" on the button or *enter the amount manually*.\n\n"
			"*Attention! Account funding is also considered a donation!*"
			" Dollars in the system are virtual points awarded for donations "
			"and they are owned by the bot owner, not the users."
			"The administration and the owner of the bot are not responsible for "
			"donated money, balance in the system and virtual points. The tariff chosen"
			" by the user can be canceled and the balance canceled at any time without "
			"giving any reason.\nAt the same time, the administration will contact and "
			"resolve disputes whenever possible and depending on the situation."
		},
		"de": {
			"ro_msg": "*" + emojiCodes.get('moneyWithWings') + " Einzahlung*\n\n"
			"Hier kannst Du Dein Konto aufladen. Durch Drücken auf den Knopf "
			"oder *manuelle Eingabe eines Betrags* erhälst Du einen Link.\n\n"
			"*Beachte: Deinen Kontostand aufzuladen wird auch als Spende betrachtet.*"
			" Jegliches Geld (in Dollar) im System entspricht virtuellen Token, "
			"welche für Spenden gutgeschrieben werden. Sie sind Eigentum des Bot-Betreibers "
			"und nicht des Nutzers. "
			"Weder die Betreiber noch der Besitzer des Bots sind verantwortlich für "
			"gespendetes Geld, Kontostände im System, und virtuelle Token. Die "
			"vom Nutzer gewählte Preisklasse und dessen Kontostand können jederzeit und "
			"ohne Angabe von Gründen storniert werden.\nNichtsdestotrotz werden die"
			" Betreiber wann immer möglich und situationsabhängig den Kontakt suchen, um"
			" Streitigkeiten aufzuklären."
		}
	},
	"money_came": {
		"ru": {
			"ro_msg": "Ваш платёж зачислен!"
		},
		"en": {
			"ro_msg": "Your payment has been credited!"
		},
		"de": {
			"ro_msg": "Deine Zahlung wurde gutgeschrieben!"
		}
	},
	"subscribe_now": {
		"ru": {
			"ro_msg": "Перейдите на страницу тарифов и выберите желаемый."
		},
		"en": {
			"ro_msg": "Go to the tariffs page and select the one you want."
		},
		"de": {
			"ro_msg": "Gehe zur Preisklassen-Übersicht und wähle aus, welche Du möchtest."
		}
	},
	"enough_to_prolongation": {
		"ru": {
			"ro_msg": "У вас достаточно средств для продления."
		},
		"en": {
			"ro_msg": "You have sufficient funds to renew."
		},
		"de": {
			"ro_msg": "Du hast ausreichende Mittel zur Erneuerung."
		}
	},
	"not_enough_to_prolongation": {
		"ru": {
			"ro_msg": "У вас недостаточно средств для продления."
		},
		"en": {
			"ro_msg": "You do not have enough funds to renew."
		},
		"de": {
			"ro_msg": "Du hast unzureichende Mittel um Dein Abonnement zu erneuern."
		}
	},
	"tariff_prolonged": {
		"ru": {
			"ro_msg": "Текущий тариф продлён."
		},
		"en": {
			"ro_msg": "The current tariff has been extended."
		},
		"de": {
			"ro_msg": "Das aktuelle Preisklassen-Abonnement wurde verlängert."
		}
	},
	"tariff_prolonged_by_daemon": {
		"ru": {
			"ro_msg": "Ваш тариф продлён! Текущие условия:"
		},
		"en": {
			"ro_msg": "Your tariff has been extended! Current conditions:"
		},
		"de": {
			"ro_msg": "Dein Abonnement wurde verlängert! Aktuelle Konditionen:"
		}
	},
	"tariff_cannot_be_prolonged_by_daemon": {
		"ru": {
			"ro_msg": "Срок действия тарифа вышел, пополните баланс."
			" Текущие условия:"
		},
		"en": {
			"ro_msg": "The tariff has expired, top up the balance. "
			"Current conditions:"
		},
		"de": {
			"ro_msg": "Die Preisklasse ist ausgelaufen. Lade Dein Konto auf! "
			"Aktuelle Konditionen:"
		}
	},
	"notificationsEnded": {
		"ru": {
			"ro_msg": "Достигнут лимит уведомлений в этом сроке действия.\n"
			"Дождитесь нового срока или перейдите на тариф с большим лимитом."
		},
		"en": {
			"ro_msg": "The notification limit has been reached within this expiration "
			"date.\nWait for a new deadline or switch to a tariff with a higher limit."
		},
		"de": {
			"ro_msg": "Die maximale Anzahl an Benachrichtigungen für die aktuelle Abrechnungsperiode"
			" wurde erreicht.\nWarte auf die nächste Periode oder wechsle in eine höhere "
			"Preisklasse mit mehr Benachrichtigungen."
		}
	},
	"award_without_s_new_user": {
		"ru": {
			"ro_msg": "По вашей ссылке зарегистрировался новый пользователь, вы были "
			"подписаны на тариф! Текущие условия:"
		},
		"en": {
			"ro_msg": "A new user has registered on your link, you were "
			"subscribed to the tariff! Current conditions:"
		},
		"de": {
			"ro_msg": "Ein neuer Nutzer hat sich mit Deinem Link registriert! "
			"Du hast ein Abonnement erhalten! Aktuelle Konditionen:"
		}
	},
	"award_with_s_new_user": {
		"ru": {
			"ro_msg": "По вашей ссылке зарегистрировался новый пользователь, ваш тариф "
			"улучшен!"
		},
		"en": {
			"ro_msg": "A new user has registered using your link, your tariff improved!"
		},
		"de": {
			"ro_msg": "Ein neuer Nutzer hat sich mit Deinem Link registriert! Deine Preisklasse "
			"hat sich verbessert!"
		}
	},
	"award_without_s_subscribed": {
		"ru": {
			"ro_msg": "Приглашённый пользователь впервые пополнил баланс, вы были "
			"подписаны на тариф! Текущие условия:"
		},
		"en": {
			"ro_msg": "The invited user has replenished the balance for the first time,"
			" you were subscribed to the tariff! Current conditions:"
		},
		"de": {
			"ro_msg": "Ein eingeladener Nutzer hat erstmals seinen Kontostand aufgeladen! "
			"Du hast ein Abonnement erhalten! Aktuelle Konditionen:"
		}
	},
	"award_with_s_subscribed": {
		"ru": {
			"ro_msg": "Приглашённый пользователь впервые пополнил баланс, тариф "
			"улучшен! Текущие условия:"
		},
		"en": {
			"ro_msg": "The invited user has replenished the balance for the first time,"
			" your tariff improved! Current conditions:"
		},
		"de": {
			"ro_msg": "Ein eingeladener Nutzer hat erstmals seinen Kontostand aufgeladen! "
			"Deine Preisklasse hat sich verbessert! Aktuelle Konditionen:"
		}
	},
	"donation": {
		"ru": {
			"ro_msg": emojiCodes.get('dollarBag') + " " + "Пожертвование"
		},
		"en": {
			"ro_msg": emojiCodes.get('dollarBag') + " " + "Donate"
		},
		"pt-BR": {
			"ro_msg": emojiCodes.get('dollarBag') + " " + "Doar"
		},
		"es": {
			"ro_msg": emojiCodes.get('dollarBag') + " " + "Donar"
		},
		"de": {
			"ro_msg": emojiCodes.get('dollarBag') + " " + "Spenden"
		},
		"he": {
			"ro_msg": emojiCodes.get('dollarBag') + " " + "תרומה"
		}
	},
	"donateMessage": {
		"ru": {
			"ro_msg": "Вы можете помочь боту с развитием!\n"
			"Отправьте сумму боту или пожертвуйте на"
			" [yasobe.ru](https://yasobe.ru/na/yourcastbot_support)."
		},
		"en": {
			"ro_msg": "You can support this bot with a donation!\n\n"
			"Please send a message with the amount in rubles. You can see the exchange"
			" rate to the US dollar under this link:"
			" https://investing.com/currencies/usd-rub.\n\n"
			"Or donate on [yasobe.ru](https://yasobe.ru/na/yourcastbot_support)."
		},
		"pt-BR": {
			"ro_msg": "Você pode ajudar o bot com uma doação!\n\n"
			"Por favor, envie o valor em rublos. Você pode descobrir a taxa de câmbio"
			" do dólar americano neste link:"
			" https: //investing.com/currencies/usd-rub.\n\n"
			"Ou faça uma doação em"
			" [yasobe.ru](https://yasobe.ru/na/yourcastbot_support)."
		},
		"es": {
			"ro_msg": "¡Puedes ayudar al bot con una donación! Por favor envíe la"
			" cantidad en rublos. Puede encontrar el tipo de cambio del dólar"
			" estadounidense en este enlace:"
			" https: //investing.com/currencies/usd-rub.\n\n"
			"O donar en [yasobe.ru](https://yasobe.ru/na/yourcastbot_support)."
		},
		"de": {
			"ro_msg": "Du kannst den Bot mit einer Spende unterstützen!\n\n"
			"Bitte sende den Betrag in Rubeln als Nachricht. Den aktuellen Wechselkurs"
			" für Euro findest Du hier:"
			" https://www.investing.com/currencies/eur-rub.\n\n"
			"Alternativ kannst Du über"
			" [yasobe.ru](https://yasobe.ru/na/yourcastbot_support) spenden."
		},
		"he": {
			"ro_msg": "אתה יכול לעזור לרובוט הזה ולתרום!\n\n"
			"אנא שלחו את הסכום ברובלים. אתה יכול לגלות את שער החליפין לדולר"
			" בקישור הזה: https://investing.com/currencies/usd-rub.\n\n"
			"או לתרום הלאה [yasobe.ru](https://yasobe.ru/na/yourcastbot_support)."
		}
	},
	"notANumber": {
		"ru": {
			"ro_msg": "Пожалуйста, введите сумму."
		},
		"en": {
			"ro_msg": "Please enter the amount in rubles."
			" You can see the exchange rate to the US dollar under this link:"
			" https://investing.com/currencies/usd-rub."
		},
		"pt-BR": {
			"ro_msg": "Por favor, insira a quantidade em rublos."
			" Você pode descobrir a taxa de câmbio para o dólar americano neste link:"
			" https://investing.com/currencies/usd-rub."
		},
		"es": {
			"ro_msg": "Por favor, entre la cantidad en rublos."
			" Puede encontrar la tasa de cambio a dólar americano en este link:"
			" https://investing.com/currencies/usd-rub."
		},
		"de": {
			"ro_msg": "Bitte gib den Betrag in Rubeln an."
			" Den aktuellen Wechselkurs für Euro"
			" findest Du hier: https://www.investing.com/currencies/eur-rub."
		},
		"he": {
			"ro_msg": "אנא הכנס את הסכום בדולרים."
			" אתה יכול למצוא את שער החליפין לדולר ב:"
			" https://investing.com/currencies/usd-rub."
		}
	},
	"paymentLinkMessage": {
		"ru": {
			"ro_msg": "Перейдите по ссылке ниже и следуйте инструкциям\n\n"
		},
		"en": {
			"ro_msg": "Follow the link below and follow the instructions\n\n"
		},
		"pt-BR": {
			"ro_msg": "Siga o link abaixo e siga as instruções\n\n"
		},
		"es": {
			"ro_msg": "Siga el link debajo y luego siga las instrucciones\n\n"
		},
		"de": {
			"ro_msg": "Klicke auf den folgenden Link und folge den"
			" Anweisungen auf der Webseite.\n\n"
		},
		"he": {
			"ro_msg": "עקוב אחר הקישור למטה ופעל על פי ההוראות\n\n"
		}
	},
	"notificationsFCDisabled": {
		"ru": {
			"ro_msg": "Не удалось получить rss ленту, "
			"поэтому уведомления для подкаста были отключены.\n"
			"Попробуйте открыть подкаст позже и включить уведомления заново."
		},
		"en": {
			"ro_msg": "Failed to get rss feed, "
			"so podcast notifications were disabled.\n"
			"Try opening the podcast later and re-enable notifications."
		},
		"pt-BR": {
			"ro_msg": "Falha ao obter feed RSS, "
			"portanto, as notificações de podcast foram desativadas.\n"
			"Tente abrir o podcast mais tarde e reative as notificações."
		},
		"es": {
			"ro_msg": "No se pudo obtener el feed rss, "
			"por lo que las notificaciones de podcast se deshabilitaron.\n"
			"Intente abrir el podcast más tarde y"
			"vuelva a habilitar las notificaciones."
		},
		"de": {
			"ro_msg": "Der RSS-Feed konnte nicht geladen werden, "
			"deshalb wurden Benachrichtigungen deaktiviert.\n"
			"Versuche den Podcast später zu öffnen und die Benachrichtigungen"
			" wieder zu aktivieren."
		},
		"he": {
			"ro_msg": "נכשלה קבלת עדכון RSS, "
			"לכן התרעות הפודקאסט הושבתו.\n"
			"נסה לפתוח מאוחר יותר את הפדקאסט והפעל מחדש התראות."
		}
	},
	"maintenance": {
		"ru": {
			"ro_msg": "Бот на обслуживании! Попробуйте позже."
		},
		"en": {
			"ro_msg": "The bot is undergoing maintenance! Please, wait for a while."
		},
		"de": {
			"ro_msg": "Der Bot ist aufgrund von Wartungsarbeiten nicht erreichbar!"
			" Bitte warte eine Weile."
		},
		"he": {
			"ro_msg": "הבוט בתחזוקה! אנא המתן."
		}
	}
}
