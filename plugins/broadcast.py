from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/GetTGLink/4178
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='ഇപ്പൊ എല്ലാവരെയും അറിയിച്ചേക്കാം...😁... 𝚊𝚗𝚍 𝚃𝚛𝚢𝚒𝚗𝚐 𝚃𝚘 𝙷𝚊𝚌𝚔 𝙼𝚢 𝙳𝚋'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"𝙱𝚛𝚘𝚍𝙲𝚊𝚜𝚝 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍:\n𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍 𝙸𝚗 {time_taken} 𝚂𝚎𝚌𝚘𝚗𝚍𝚜.\n\n𝚃𝚘𝚝𝚊𝚕 𝚄𝚜𝚎𝚛𝚜 {total_users}\n𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍: {done} / {total_users}\n𝚂𝚞𝚌𝚌𝚎𝚜: {success}\n𝚆𝚑𝚢 𝙱𝚕𝚘𝚌𝚔 𝙼𝚎: {blocked}\n𝚆𝚊𝚜𝚝𝚎𝚍: {deleted}")
