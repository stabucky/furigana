import streamlit as st
import furigana

def main():
  st.title("Furigana")
  grades=(
    "小学1年生向け",
    "小学2年生向け",
    "小学3年生向け",
    "小学4年生向け",
    "小学5年生向け",
    "小学6年生向け",
    "中学生以上向け",
    "一般向け",
  )
  with st.form("my_form"):
    textarea_val=st.text_area("Texts",value="",placeholder="ここに文章をセット。")

    grade_val=st.selectbox("Grade",grades)
    submitted = st.form_submit_button("Submit")
  if submitted:
    if not textarea_val == "":
      for i,w in enumerate(grades):
        if w == grade_val:
          grade_int = i + 1
          break
      result=furigana.make_furigana(textarea_val, grade=grade_int)
      st.info(result)

  st.write("&copy;2022You Look Too Cool")
  


if __name__ == "__main__":
  main()
