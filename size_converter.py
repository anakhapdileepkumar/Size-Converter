import streamlit as st

def convert_to_inches(value, unit):
    if unit == 'cm':
        return value / 2.54
    return value

def get_size_for_hm(gender, chest):
    if gender == 'men':
        if chest < 36:
            return 'S'
        elif chest < 40:
            return 'M'
        elif chest < 44:
            return 'L'
        else:
            return 'XL'
    else:
        if chest < 32:
            return 'XS'
        elif chest < 34:
            return 'S'
        elif chest < 36:
            return 'M'
        elif chest < 38:
            return 'L'
        else:
            return 'XL'

def get_size_for_zara(gender, chest):
    if gender == 'men':
        if chest < 36:
            return '36'
        elif chest < 38:
            return '38'
        elif chest < 40:
            return '40'
        elif chest < 42:
            return '42'
        else:
            return '44'
    else:
        if chest < 32:
            return '34'
        elif chest < 34:
            return '36'
        elif chest < 36:
            return '38'
        elif chest < 38:
            return '40'
        else:
            return '42'

def main():
    st.title("Body Measurement to Clothing Size Converter")

    gender = st.selectbox("Select Gender", options=['men', 'women'])
    unit = st.selectbox("Select Measurement Unit", options=['inches', 'cm'])

    chest = st.number_input("Chest/Bust Measurement", min_value=0.0, step=0.1)
    waist = st.number_input("Waist Measurement", min_value=0.0, step=0.1)
    hips = st.number_input("Hips Measurement", min_value=0.0, step=0.1)

    if st.button("Convert"):
        chest_in = convert_to_inches(chest, unit)
        waist_in = convert_to_inches(waist, unit)
        hips_in = convert_to_inches(hips, unit)

        hm_size = get_size_for_hm(gender, chest_in)
        zara_size = get_size_for_zara(gender, chest_in)

        st.write("### Estimated Clothing Sizes:")
        st.write(f"H&M Size: **{hm_size}**")
        st.write(f"Zara Size: **{zara_size}**")

if __name__ == "__main__":
    main()
