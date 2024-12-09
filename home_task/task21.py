# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""
list_ = template.split("\n")
print(list_)
ready_html = ""
for i in list_:
        for key in page:
                if key in i:
                        i = i.replace("?", page[key])
        ready_html = ready_html + i + "\n"
f = open("index.html", "w+t")
f.write(f""" {ready_html}""")
f.close()

