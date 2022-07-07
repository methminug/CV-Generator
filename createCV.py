import json
import os
from configureCV import add_cv_configs
import subprocess


# ----------- Configuring the CV layout -----------
add_cv_configs()

# ----------- Order of sections in CV -----------
cv_sections = ['overview', 'education', 'skills',
               'experience', 'awards', 'extracurricular']

# ----------- Create CV Header -----------
with open("sections/personalinfo.json", 'r') as file:
    personal_info = json.load(file)
    personal_info_section = ""
    for tag, value in personal_info.items():
        if(value == ""):
            pass
        elif(tag == "name"):
            personal_info_section += r"\name{%s}{%s}" % (
                value.split(" ")[0], value.split(" ")[1])
        else:
            personal_info_section += r"\%s{%s}" % (tag, value)

header_content = r'''
%s

\begin{document}

\makecvheader[C]

\makecvfooter
  {\today}
  {%s}
  {\thepage}
''' % (personal_info_section, personal_info.get("name"))
with open('cv.tex', 'a') as f:
    f.write(header_content)

# ----------- Create CV Body -----------
for section_file in cv_sections:
    with open(os.path.join("sections", section_file+".json"), 'r') as file:
        section_data = json.load(file)
        if(section_data.get('records') is None):
            section_records = section_data.get('description')
        else:
            section_records = r''''''
            for record in section_data.get('records'):
                record_content = r'''
                  \%s
                ''' % (section_data.get('tagname'))
                for record_data in record:
                    item_list = ""
                    if(isinstance(record.get(record_data), list)):
                        item_list = r'''
                        {
                          \begin{cvitems}
                        '''
                        for item in record.get(record_data):
                            item_list += '    \item{%s}' % (item)
                        item_list += r'''
                          \end{cvitems}
                        }'''
                    else:
                        record_content = record_content + \
                            '''{%s}''' % (record.get(record_data))
                section_records += record_content+item_list
        section_content = r'''
        \cvsection{%s}

        \begin{%s}

        %s
        \end{%s}

        ''' % (section_data.get('title'), section_data.get('sectionname'), section_records, section_data.get('sectionname'))
        with open('cv.tex', 'a') as f:
            f.write(section_content)

with open('cv.tex', 'a') as f:
    f.write(r"\end{document}")
