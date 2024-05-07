from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y")

hora_formatada = agora.strftime("%H:%M")

print("Data:", data_formatada)
print("Hora:", hora_formatada)
