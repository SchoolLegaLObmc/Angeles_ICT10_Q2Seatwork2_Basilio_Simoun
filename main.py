
from pyscript import document, display




def process_input(event=None):
    
    
    english = int(document.getElementById("english").value) * 4
    math = int(document.getElementById("math").value) * 4 
    ict = int(document.getElementById("ict").value) * 1
    filipino = int(document.getElementById("filipino").value) * 3
    science = int(document.getElementById("science").value) * 4
    social_studies = int(document.getElementById("social-studies").value) * 3
    pe = int(document.getElementById("pe").value) * 1
    ve = int(document.getElementById("ve").value) * 1
    TLE = int(document.getElementById("TLE").value)* 1


    english_raw =english / 4
    math_raw  =math / 4
    ict_raw  =ict * 1
    filipino_raw  =filipino / 3
    science_raw =science / 4
    social_studies_raw =social_studies /3
    pe_raw  =pe * 1
    ve_raw  =ve * 1
    TLE_raw  =TLE * 1


    name_first = (document.getElementById("name2").value or "").strip()
    name_last = (document.getElementById("name").value or "").strip()
    display_name = name_first + name_last


    subject = (english, math, ict, filipino, science, social_studies, pe, ve, TLE)



    Average = (english + math + ict + filipino + science + social_studies + pe + ve + TLE) /22

    result = f"""
    <div class="result-card">
      <div class="result-header">Name: {display_name}</div>
      <div class="result-box">
        Science: {science_raw}<br>
        Math: {math_raw}<br>
        English: {english_raw}<br>
        Filipino: {filipino_raw}<br>
        ICT: {ict_raw}<br>
        PE: {pe_raw}
      </div>
    </div>
    <div class="gwa-box">Your general weighted average is {Average:.2f}</div>
    """
    output_element = document.getElementById("output")
    output_element.innerHTML = result




