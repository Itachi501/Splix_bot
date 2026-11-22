
import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


# Группа команд аккаунтов
acc = app_commands.Group(name="acc", description="Поиск аккаунтов")

@acc.command(name="gid", description="Поиск аккаунта по Global ID")
async def acc_gid(interaction: discord.Interaction, gid: str):
    await interaction.response.send_message(
        f"Поиск аккаунта по Global ID: {gid}\nБаза данных пока не подключена."
    )

@acc.command(name="name", description="Поиск по серверу и никнейму")
async def acc_name(interaction: discord.Interaction, server: str, nickname: str):
    await interaction.response.send_message(
        f"Сервер: {server}\nНикнейм: {nickname}\nБаза данных пока не подключена."
    )


# Группа блокировок
bans = app_commands.Group(name="bans", description="Поиск блокировок")

@bans.command(name="gid", description="Поиск блокировки по Global ID")
async def bans_gid(interaction: discord.Interaction, gid: str):
    await interaction.response.send_message(
        f"Поиск блокировки по GID: {gid}\nБаза данных пока не подключена."
    )

@bans.command(name="player", description="Поиск блокировки игрока")
async def bans_player(interaction: discord.Interaction, server: str, nickname: str):
    await interaction.response.send_message(
        f"Сервер: {server}\nИгрок: {nickname}\nБаза данных пока не подключена."
    )


# Группа поиска
search = app_commands.Group(name="search", description="Поиск игроков")

@search.command(name="name", description="Поиск по имени")
async def search_name(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Поиск по имени: {name}")

@search.command(name="nick", description="Поиск по Alias Name")
async def search_nick(interaction: discord.Interaction, nick: str):
    await interaction.response.send_message(f"Поиск по Alias Name: {nick}")

@search.command(name="test", description="Поиск по серверу и никнейму")
async def search_test(interaction: discord.Interaction, server: str, nickname: str):
    await interaction.response.send_message(
        f"Сервер: {server}\nНикнейм: {nickname}"
    )

@search.command(name="ds", description="Поиск по Discord")
async def search_ds(interaction: discord.Interaction, user: str):
    await interaction.response.send_message(f"Поиск по Discord: {user}")

@search.command(name="gid", description="Поиск по Global ID")
async def search_gid(interaction: discord.Interaction, gid: str):
    await interaction.response.send_message(f"Поиск по GID: {gid}")

@search.command(name="id", description="Поиск по игровому ID")
async def search_id(interaction: discord.Interaction, player_id: str):
    await interaction.response.send_message(f"Поиск по ID: {player_id}")


# Остальные команды
@bot.tree.command(name="admins", description="Список администраторов")
async def admins(interaction: discord.Interaction):
    await interaction.response.send_message("Список администраторов пока не подключён.")

@bot.tree.command(name="complaints", description="Список жалоб")
async def complaints(interaction: discord.Interaction):
    await interaction.response.send_message("Список жалоб пока не подключён.")

@bot.tree.command(name="help", description="Список команд")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Команды Splix_bot:\n"
        "/acc gid, /acc name\n"
        "/admins\n"
        "/bans gid, /bans player\n"
        "/complaints\n"
        "/help\n"
        "/jb\n"
        "/norma\n"
        "/ping\n"
        "/report\n"
        "/reports\n"
        "/search name, nick, test, ds, gid, id"
    )

@bot.tree.command(name="jb", description="Просмотр закрытых жалоб")
async def jb(interaction: discord.Interaction):
    await interaction.response.send_message("Закрытые жалобы пока не подключены.")

@bot.tree.command(name="norma", description="Проверка нормы администраторов")
async def norma(interaction: discord.Interaction):
    await interaction.response.send_message("Данные нормы пока не подключены.")

@bot.tree.command(name="ping", description="Проверка работы бота")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Задержка: {round(bot.latency * 1000)} мс")

@bot.tree.command(name="report", description="Статистика репортов")
async def report(interaction: discord.Interaction):
    await interaction.response.send_message("Статистика репортов пока не подключена.")

@bot.tree.command(name="reports", description="Отчёты администраторов")
async def reports(interaction: discord.Interaction):
    await interaction.response.send_message("Отчёты пока не подключены.")


# Регистрация групп команд
bot.tree.add_command(acc)
bot.tree.add_command(bans)
bot.tree.add_command(search)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Splix_bot запущен: {bot.user}")


if TOKEN:
    bot.run(TOKEN)
else:
    print("Ошибка: не найден DISCORD_TOKEN")
