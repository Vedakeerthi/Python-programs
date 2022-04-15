# # WIKIPEDIA MODULE

# INSTALLING THE MODULE

pip install wikipedia


# IMPORTING THE MODULE AND GETTING A SUMMARY ABOUT THE TOPIC LAND DEGRADATION

import wikipedia
r = wikipedia.summary("land degradation",sentences = 10)
print(r)


# SEARCHING A TOPIC ABOUT PYTHON

r = wikipedia.search("python", results =3)
print(r)


# THE SUMMARY IS USED TO SUMMARISE THE TOPIC GIVEN
# THE SEARCH IS USED TO SEARCH THE DIFFERENT TOPICS AVAILABLE IN WIKIPEDIA UPTO A GIVEN RESULTS


r = wikipedia.page("python(programming language)")
print(r.html)
print(r.title)
print(r.images)


# THE PAGE IS USED TO GAIN THE THINGS THAT ARE PRESENT IN THE PAGE
# HERE I HAVE GOT THE PAGE IN HTML FORMAT, THE TITLE OF THE PAGE, AND ALSO THE IMAGES PRESENT IN THE PAGE


wikipedia.set_lang("hi")
print(wikipedia.summary("land degradation",sentences = 10))


# HERE THE SET LANGUAGE IS USED TO TRANSLATE TO HINDI AND PRINT THE LANDDEGRADATION IN HINDI


# SO THESE ARE THE IMPORTANT FEATURES USED IN WIKIPEDIA MODULE...
  # SUMMARY;SENTENCES
  # SEARCH;RESULTS
  # PAGE;TITLE, IMAGE, LINKS, HTML EXTRACTION 
  # SET_LANG

