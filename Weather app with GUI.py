from tkinter import *
from tkinter import ttk
import requests
window = Tk()
window.title("Weather App")
window.config(bg= "light blue")
window.geometry("600x600")


def data_get():
    try:
        city = city_name.get()
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b102b0d2cbcc149cb68ce97704aad006").json()   
        weather_climate1.config(text= data["weather"][0]["main"])
        Weather_Description1.config(text= data["weather"][0]["description"])
        Temperature1.config(text= str(int(data["main"]["temp"]-273.15)) + " °C")
        Pressure1.config(text= data["main"]["pressure"])
        Humidity1.config(text= data["main"]["humidity"])
        Visibility1.config(text= data["visibility"])
    except Exception as e:
        # Display a message if an exception occurs
        weather_climate1.config(text="N/A")
        Weather_Description1.config(text="N/A")
        Temperature1.config(text="N/A")
        Pressure1.config(text="N/A")
        Humidity1.config(text="N/A")
        Visibility1.config(text="N/A")
        print("An error occurred:", e)

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
weather_climate.place(x=125, y=250, height=40, width=150)
# :
weather_climate1 = Label(window, text=" ", font=("Times New Roman", 15))
weather_climate1.place(x=275, y=250, height=40, width=200)

#Weather_Description Label
Weather_Description = Label(window, text="Weather Description", font=("Times New Roman", 15))
Weather_Description.place(x=125, y=300, height=40, width=180)
# :
Weather_Description1 = Label(window, text=" ", font=("Times New Roman", 15))
Weather_Description1.place(x=300, y=300, height=40, width=175)

#Temperature Label
Temperature = Label(window, text="Temperature ", font=("Times New Roman", 15))
Temperature.place(x=125, y=350, height=40, width=170)
# :
Temperature1 = Label(window, text=" ", font=("Times New Roman", 15))
Temperature1.place(x=295, y=350, height=40, width=180)

#Pressure Label
Pressure = Label(window, text="Pressure", font=("Times New Roman", 15))
Pressure.place(x=125, y=400, height=40, width=150)
# :
Pressure1 = Label(window, text=" ", font=("Times New Roman", 15))
Pressure1.place(x=275, y=400, height=40, width=200)

#Pressure Label
Humidity = Label(window, text="Humidity", font=("Times New Roman", 15))
Humidity.place(x=125, y=450, height=40, width=150)
# :
Humidity1 = Label(window, text="", font=("Times New Roman", 15))
Humidity1.place(x=275, y=450, height=40, width=200)

#Pressure Label
Visibility = Label(window, text="Visibility", font=("Times New Roman", 15))
Visibility.place(x=125, y=500, height=40, width=150)
# :
Visibility1 = Label(window, text=" ", font=("Times New Roman", 15))
Visibility1.place(x=275, y=500, height=40, width=200)


window.mainloop()

