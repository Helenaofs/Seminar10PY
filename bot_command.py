from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from log import *

operation = 0
operands = []


def help_command(update: Update, context: CallbackContext):
    global operation 
    operation = 0

    calc = ""
    calc += "КАЛЬКУЛЯТОР\n"
    calc += "Выберите действие на свой вкус:\n"
    calc += "Сложение /sum\n"
    calc += "Вычитание /sub\n"
    calc += "Умножение /mult\n"
    calc += "Деление /div\n"
    calc += "! Комплексные числа вводить через пробел"
    update.message.reply_text(calc)


def sum_command(update: Update, context: CallbackContext):
    global operation
    operation = 1


def sub_command(update: Update, context: CallbackContext):
    global operation
    operation = 2


def mult_command(update: Update, context: CallbackContext):
    global operation
    operation = 3


def div_command(update: Update, context: CallbackContext):
    global operation
    operation = 4
  

def analize_command(update: Update, context: CallbackContext):
    global operation, operands
    calc = ""

    if operation:
        if len(operands)<2:
            msg = update.message.text
            
            if " " in msg and msg.split(" ")[0].isdigit() and msg.split(" ")[1].isdigit():
                operands.append(complex(float(msg.split(" ")[0]), float(msg.split(" ")[1])))
                update.message.reply_text(f"Комплексное число {operands[-1]}")
            elif msg.isdigit():
                operands.append(float(msg))
            else:
                update.message.reply_text("Неправильный ввод. Попробуйте еще раз!")
        if len(operands) == 2:
            match operation:
                case 1:
                    calc = f"{operands[0]} + {operands[1]} = {operands[0]+operands[1]}"
                case 2:
                    calc = f"{operands[0]} - {operands[1]} = {operands[0]-operands[1]}"
                case 3:
                    calc = f"{operands[0]} * {operands[1]} = {operands[0]*operands[1]}"
                case 4:
                    calc = f"{operands[0]} / {operands[1]} = {operands[0]/operands[1]}"
            log(update,context,calc)
            update.message.reply_text(calc)
            operands=[]
            operation=0
            