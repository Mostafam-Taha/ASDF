from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ضع توكن البوت الخاص بك هنا
TOKEN: Final = '6898971699:AAEJuQsk78Ye5knm7pmqTir3xN4AAdGhX58'
BOT_USERNAME: Final = '@sahatalllmbot'

# دالة لبدء المحادثة
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحباً! كيف يمكنني مساعدتك؟')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحباً! كيفasdfsadfasdfafd يمكنني مساعدتك؟')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحباً! كيف يمكنasdfasdfasdfasdfasdfasdfasdfsadfني مساعدتك؟')

# دالة لعرض المساعدة
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "الأوامر المتاحة:\n/start - بدء المحادثة\n/help - عرض هذه المساعدة"
    await update.message.reply_text(help_text)

# دالة لإرسال صورة
async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('path_to_your_image.jpg', 'rb') as photo:  # ضع مسار الصورة هنا
        await update.message.reply_photo(photo=InputFile(photo))

# الدالة الرئيسية لتشغيل البوت
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة معالجات الأوامر والرسائل
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))  # إضافة أمر المساعدة
    app.add_handler(CommandHandler('photo', send_photo))  # إضافة أمر لإرسال صورة
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # بدء البوت
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
