import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "Gersik": {  # Add emission factors for Gersik
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    },
    "Bangkalan": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    },
    "Mojokerto": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    },
    "Surabaya": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    },
    "Sidoarjo": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    },
    "Lamongan": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Streamlit app code
st.title("Tera Carbon Calculator 🌱")

# User inputs
st.subheader("🌍 Pilih Kotamu")
country = st.selectbox("Pilih", ["Surabaya", "Bangkalan", "Mojokerto", "Gersik", "Sidoarjo", "Lamongan"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Jarak tempat tinggal Ke Kampus (km)")
    distance = st.slider("Jarak", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Penggunaan Listrik Bulanan (kWh)")
    electricity = st.slider("Listrik", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🍽️ Sampah yang dihasilkan (kg)")
    waste = st.slider("Sampah", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Porsi Makan Tiap Hari")
    meals = st.number_input("Makan", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Caritau emisi mu!"):

    # Display results
    st.header("Hasilnya")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Emisi Carbonmu")
        st.info(f"🚗 Transportasi: {transportation_emissions} tonnes CO2 per tahun")
        st.info(f"💡 Listrik: {electricity_emissions} tonnes CO2 per tahun")
        st.info(f"🍽️ Makanan: {diet_emissions} tonnes CO2 per tahun")
        st.info(f"🗑️ Sampah: {waste_emissions} tonnes CO2 per tahun")

    with col4:
        st.subheader("Total Jejak Carbonmu")
        st.success(f"👣 Emisimu menjadi jejak karbon sebanyak: {total_emissions} ton CO2 per tahun 💨")
        st.success(f"🦖 Pesan dari Tera!!, Yuk Bareng Bareng Kendalikan Carbonmu dan Gunakan Energi dengan Bijak! 🌿🌎 ")
        st.warning("Indonesia menargetkan untuk menurunkan emisi GRK sektor energi sebesar 31,89% dengan usaha sendiri dan sebesar 43,20% dengan dukungan dunia internasional pada tahun 2030, Implementasi EBT (51,30 juta ton CO2e), Aplikasi efisiensi energi telah berhasil mengurangi 31,76 juta ton CO2e, sementara penerapan bahan bakar rendah karbon seperti gas alam mengurangi 15,55 juta ton CO2e. Penggunaan teknologi pembangkit bersih serta berbagai kegiatan lainnya juga telah berkontribusi mengurangi 13,33 juta ton CO2e dan 15,63 juta ton CO2e secara berturut-turut. Kamu juga bisa berkontribusi dengan cara menggunakan energi secara efisien, memilih bahan bakar rendah karbon, dan mendukung penggunaan teknologi bersih untuk menjaga lingkungan dan masa depan yang lebih baik! 🌿💡✨")

        st.markdown("[🌏Bantu Untuk Keberlanjutan bumi yang lebih baik ](https://forms.gle/kgEKZiqXYUNyx8Wx8)")

with st.expander('About', expanded=True):
        st.write('''
            - Geotera: [Tera](https://www.instagram.com/thegeotera/).
            ''')
