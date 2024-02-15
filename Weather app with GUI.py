from tkinter import *
from tkinter import ttk
import requests
window = Tk()
window.title("Weather App")
window.config(bg= "light blue")
window.geometry("600x600")

# make a function
def data_get():

    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b102b0d2cbcc149cb68ce97704aad006").json()   
    weather_climate1.config(text= data["weather"][0]["main"])
    Weather_Description1.config(text= data["weather"][0]["description"])
    Temperature1.config(text= str(int(data["main"]["temp"]-273.15)))
    Pressure1.config(text= data["main"]["pressure"])

# Weather app title display
name_label =  Label(window, text="Weather App", font=("Times New Roman", 25, "bold"))
name_label.place(x=75, y=50, height=50, width=450)

#list of cities display
city_name = StringVar()
list_name = [
    "Ahmadpur East",
    "Ahmed Nager Chatha",
    "Ali Khan Abad",
    "Alipur",
    "Arifwala",
    "Attock",
    "Bhera",
    "Bhalwal",
    "Bahawalnagar",
    "Bahawalpur",
    "Bhakkar",
    "Burewala",
    "Chenab Nagar",
    "Chillianwala",
    "Choa Saidanshah",
    "Chakwal",
    "Chak Jhumra",
    "Chichawatni",
    "Chiniot",
    "Chishtian",
    "Chunian",
    "Dajkot",
    "Daska",
    "Davispur",
    "Darya Khan",
    "Dera Ghazi Khan",
    "Dhaular",
    "Dina",
    "Dinga",
    "Dhudial Chakwal",
    "Dipalpur",
    "Faisalabad",
    "Fateh Jang",
    "Ghakhar Mandi",
    "Gojra",
    "Gujranwala",
    "Gujrat",
    "Gujar Khan",
    "Harappa",
    "Hafizabad",
    "Haroonabad",
    "Hasilpur",
    "Haveli Lakha",
    "Islamabad",
    "Jalalpur Jattan",
    "Jampur",
    "Jaranwala",
    "Jhang",
    "Jhelum",
    "Jauharabad",
    "Kallar Syedan",
    "Kalabagh",
    "Karor Lal Esan",
    "Karachi",
    "Kasur",
    "Kamalia",
    "Kāmoke",
    "Khanewal",
    "Khanpur",
    "Khanqah Sharif",
    "Kharian",
    "Khushab",
    "Kot Adu",
    "Lahore",
    "Lalamusa",
    "Layyah",
    "Lawa Chakwal",
    "Liaquat Pur",
    "Lodhran",
    "Malakwal",
    "Mamoori",
    "Mailsi",
    "Mandi Bahauddin",
    "Mian Channu",
    "Mianwali",
    "Miani",
    "Multan",
    "Murree",
    "Muridke",
    "Mianwali Bangla",
    "Muzaffargarh",
    "Narowal",
    "Nankana Sahib",
    "Okara",
    "Pakpattan",
    "Pattoki",
    "Pindi Bhattian",
    "Pind Dadan Khan",
    "Pir Mahal",
    "Qaimpur",
    "Qila Didar Singh",
    "Raiwind",
    "Rajanpur",
    "Rahim Yar Khan",
    "Rawalpindi",
    "Renala Khurd",
    "Sadiqabad",
    "Sagri",
    "Sahiwal",
    "Sambrial",
    "Samundri",
    "Sangla Hill",
    "Sarai Alamgir",
    "Sargodha",
    "Shakargarh",
    "Sheikhupura",
    "Shujaabad",
    "Sialkot",
    "Sohawa",
    "Soianwala",
    "Siranwali",
    "Tandlianwala",
    "Talagang",
    "Taxila",
    "Toba Tek Singh",
    "Vehari",
    "Wah Cantonment",
    "Wazirabad",
    "Yazman",
    "Zafarwal"
  ]
com = ttk.Combobox(window, text="Weather App",values= list_name, font=("Times New Roman", 15), textvariable=city_name)
com.place(x=75, y=120, height=40, width=450)

#done button
done_button = Button(window, text="Done", font=("Times New Roman", 15), command=data_get)
done_button.place(x=250, y=190, height=40, width=100)

#weather_climate button
weather_climate = Label(window, text="Weather Climate", font=("Times New Roman", 15))
weather_climate.place(x=50, y=250, height=30, width=150)
# :
weather_climate1 = Label(window, text=" ", font=("Times New Roman", 15))
weather_climate1.place(x=250, y=250, height=30, width=200)

#Weather_Description Label
Weather_Description = Label(window, text="Weather Description", font=("Times New Roman", 15))
Weather_Description.place(x=50, y=300, height=40, width=180)
# :
Weather_Description1 = Label(window, text=" ", font=("Times New Roman", 15))
Weather_Description1.place(x=250, y=300, height=40, width=200)

#Temperature Label
Temperature = Label(window, text="Temperature", font=("Times New Roman", 15))
Temperature.place(x=50, y=350, height=40, width=150)
# :
Temperature1 = Label(window, text=":", font=("Times New Roman", 15))
Temperature1.place(x=250, y=350, height=40, width=140)

#Pressure Label
Pressure = Label(window, text="Pressure", font=("Times New Roman", 15))
Pressure.place(x=50, y=400, height=40, width=100)
# :
Pressure1 = Label(window, text=": cds", font=("Times New Roman", 15))
Pressure1.place(x=190, y=400, height=40, width=200)

# #done Label
# done_Label = Label(window, text="Done", font=("Times New Roman", 15))
# done_Label.place(x=250, y=190, height=40, width=100)
# #done Label
# done_Label = Label(window, text="Done", font=("Times New Roman", 15))
# done_Label.place(x=250, y=190, height=40, width=100)
# #done Label
# done_Label = Label(window, text="Done", font=("Times New Roman", 15))
# done_Label.place(x=250, y=190, height=40, width=100)
# #done Label
# done_Label = Label(window, text="Done", font=("Times New Roman", 15))
# done_button.place(x=250, y=190, height=40, width=100)
window.mainloop()

