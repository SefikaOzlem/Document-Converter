import csv
import sys
import xml.etree.ElementTree as ET
import json
from lxml import etree
from io import StringIO

def type1(input_filename,output_filename):             # CSV TO XML CONVERTER METHOD 
  k=0         # control how many times the loop will turn 
  Unitype=[]  # temp to university type list
  Uniname=[]  # temp to university name list
  Faclty=[]   # temp to faculty list
  Program_id=[]  # temp to program id list
  Program_name=[] # temp to program name list 
  Language=[]    # temp to language list
  Second=[]     # temp to education type list (ikinci öğretim or NO)
  Grant=[]      # temp to grant list
  Period=[]   # temp to education time list
  Field=[]    # temp to type of score list
  Quota=[]    # temp to quota list
  Spec=[]     # temp school degree quota list
  Order=[]    #temp to last min order list
  Score=[]    # temp to last score list
  b=0         # temp where loop starts
  with open (input_filename,'r') as file:     # this part read csv file and append elements into the lists 
    reader =csv.reader(file,delimiter=';')
    for row in reader:
        Unitype.append(row[0])
        Uniname.append(row[1])
        Faclty.append(row[2])
        Program_id.append(row[3])
        Program_name.append(row[4])
        Language.append(row[5])
        Second.append(row[6])
        Grant.append(row[7])
        Period.append(row[8])
        Field.append(row[9])
        Quota.append(row[10])
        Spec.append(row[11])
        Order.append(row[12])
        Score.append(row[13])
    root=ET.Element("departments") # root of xml file                        # this part writing xml using xmltree library 
    root.text="\n     "     # for go to buttom line 
    b=b+1                  # csv file items start to first (1.) line 
    k=k+13                # for university control. For example DEU has thirteen line in csv file  
    for c in range(0,8):     # Informations of eight universit in csv file 
        name_uni=ET.SubElement(root,"university",name=Uniname[k],uType=Unitype[k])
        name_uni.tail="\n"
        for i in range(b,k+1):
            items=ET.SubElement(name_uni,"item",faculty=Faclty[i],Id=Program_id[i])  #temp to program id and faculty 
            if "".__eq__(Second[i]):
                Second[i]="NO"
            if 'İngilizce'.__eq__(Language[i]):
                Language[i]='en'
            if '-'.__eq__(Score[i]):
                Score[i]=""
            cv=ET.SubElement(items,"name",lang=Language[i],second=Second[i]) # temp to name language and second informations 
            pr=ET.SubElement(items,"period")                                 # temp to education time 
            qt=ET.SubElement(items,"quota",spec=Spec[i])                   # temp to quota line informations 
            fl=ET.SubElement(items,"field")                               # temp to score type 
            lm=ET.SubElement(items,"last_min_score",order=Order[i])         # temp to last min score and order 
            gr=ET.SubElement(items,"grant")                               # temp to grant information 
            lm.text=Score[i]   # last min order information 
            fl.text=Field[i]   #score type information 
            qt.text=Quota[i]   # quota information 
            pr.text=Period[i]   # education time 
            cv.text=Program_name[i] # program name information 
            gr.text=Grant[i]          # grant information 
            gr.tail="\n        "           # for line break in this parts 
            lm.tail="\n            "
            fl.tail="\n            "
            qt.tail="\n            "
            pr.tail="\n            "
            cv.tail="\n            "
            items.text="\n            "  
            if i==13:                     # the number of the line where the DEU ends 
                b=14                      # the number of the line where the Ege University stars 
                k=22                      # the number of the line where the Ege University ends
            else:
                items.tail="\n        "  
            if i==22:                     # the number of the line where the Ege University ends  
                b=23                      # the number of the line where the Yaşar University stars 
                k=50                      # the number of the line where the Yaşar  University ends
            else:
                items.tail="\n        "        
            if i==50:                      # the number of the line where the Yaşar University ends  
                b=51                       # the number of the line where the İzmir Ekonomi University stars 
                k=78                       # the number of the line where the İzmir Ekonomi University ends
            else:
                items.tail="\n        "
            if i==78:                       # the number of the line where the İzmir Ekonomi University ends  
                b=79                        # the number of the line where the İYTE University stars 
                k=88                        # the number of the line where the İYTE University ends
            else:
                items.tail="\n        "
            if i==88:                      # the number of the line where the İYTE University ends  
                b=89                       # the number of the line where the Bakırçay University stars 
                k=92                       # the number of the line where the Bakırçay University ends
            else:
                items.tail="\n        "
            if i==92:                        # the number of the line where the Bakırçay ends  
                b=93                         # the number of the line where the Demorasi University stars 
                k=97                         # the number of the line where the Demokrasi University ends
            else:
                items.tail="\n        "
            if i==97:                      # the number of the line where the Demokrasi University ends  
                b=98                       # the number of the line where the İKÇU stars 
                k=105                      # the number of the line where the İKÇU ends
            else:
                items.tail="\n        "
            name_uni.tail="\n    "
            name_uni.text="\n        "
        items.tail="\n    "    
        if c==7:
              name_uni.tail="\n"   
    tree=ET.ElementTree(root)
    tree.write(output_filename,encoding='utf-8')     # xml file write using tree 

def type2(input_filename,output_filename):            #CSV FILE TO XML FILE CONVERT METHOD 
  xml_filename=input_filename
  tree=ET.parse(xml_filename)
  root=tree.getroot()
  with open(output_filename,'w',newline='') as Emp_data:    
    csvwriter=csv.writer(Emp_data,delimiter=";")
    Emp_data.write("University Type,University Name,Faculty,Program Id,Program Name,Language,Second,Qrant,Period,Field,Quota,Spec,Last Min Score Order,Last Min Score\n")
    for member in root.findall('university'):  # the loop will turn for every university 
        emp_nodes=[]   #temp to xml elements 
        uni_type=member.get('uType')  
        fac=member.find('item').get('faculty')
        uni_name=member.get('name')
        for ite in member.findall('item'): # the loop is informations of the university and append to emp_nodes list 
            emp_nodes.append(uni_type)
            emp_nodes.append(uni_name)
            emp_nodes.append(fac)
            ıd=ite.get('Id')
            emp_nodes.append(ıd)
            program=ite.find('name').text
            emp_nodes.append(program)
            language=ite.find('name').get('lang')
            if 'en'.__eq__(language):
                language='İngilizce'
            emp_nodes.append(language)
            second=ite.find('name').get('second')
            if second.__eq__('NO'):
                  second=""
            emp_nodes.append(second)
            qrant=ite.find('grant').text
            emp_nodes.append(qrant)
            period=ite.find('period').text
            emp_nodes.append(period)
            field=ite.find('field').text
            emp_nodes.append(field)
            quota=ite.find('quota').text
            emp_nodes.append(quota)
            quota_of_degree=ite.find('quota').get('spec')
            emp_nodes.append(quota_of_degree)
            last_min_score_order=ite.find('last_min_score').get('order')
            emp_nodes.append(last_min_score_order)
            last_min_score=ite.find('last_min_score').text
            if '-'.__eq__(last_min_score):
                  last_min_score=""
            emp_nodes.append(last_min_score)
            csvwriter.writerow(emp_nodes)    # write the emp nodes list in csv file 
            emp_nodes.clear()   

def type3(input_filename,output_filename):        # XML FILE TO JSON FILE CONVERT METHOD 
  xml_filename=input_filename
  tree=ET.parse(xml_filename)
  root=tree.getroot()
  program_id=[]          #temp to program ıd list 
  universty_name=[]      # temp to university name list
  uni_typ=[]            # temp to university type list
  faculty=[]            #temp to faculty list
  Langu=[]              # temp to language list
  Second=[]            #temp to education time list 
  program_name=[]       # temp to program name list 
  Period=[]            # temp to education time list
  Quota=[]             # temp to quota of university list
  Spec=[]              #temp to school degree quota list 
  Field=[]            # temp to score type list
  last_score=[]        # temp to last min score list
  last_order=[]        #temp to last min order list
  Grant=[]            #temp to grant list
  for member in root.findall('university'):
      uni_type=member.get('uType') 
      uni_typ.append(uni_type) 
      fac=member.find('item').get('faculty')
      faculty.append(fac)
      uni_name=member.get('name')
      universty_name.append(uni_name)   
      for ite in member.findall('item'):
            ıd=ite.get('Id')
            program_id.append(ıd)
            program=ite.find('name').text
            program_name.append(program)
            language=ite.find('name').get('lang')
            if "".__eq__(language):
                language=None
            Langu.append(language)
            second=ite.find('name').get('second')
            Second.append(second)
            qrant=ite.find('grant').text
            Grant.append(qrant)
            period=ite.find('period').text
            Period.append(period)
            field=ite.find('field').text
            Field.append(field)
            quota=ite.find('quota').text
            Quota.append(quota)
            quota_of_degree=ite.find('quota').get('spec')
            if "".__eq__(quota_of_degree):
                quota_of_degree=None
            Spec.append(quota_of_degree)
            last_min_score_order=ite.find('last_min_score').get('order')
            if "".__eq__(last_min_score_order):
                last_min_score_order=None
            last_order.append(last_min_score_order)
            last_min_score=ite.find('last_min_score').text
            last_score.append(last_min_score)                          
  with open(output_filename,'w',newline='') as Emp_data:
      DEU_Items=[]   # temp to all items of DOKUZ EYLUL UNIVERSITY list
      EU_Items=[]    # temp to all items of EGE UNIVERSITY   list 
      YAS_Items=[]   # temp to all items of YAŞAR  UNIVERSITY list
      EKO_Items=[]   # temp to all items of İZMİR EKONOMİ  UNIVERSITY list
      IYTE_Items=[]  # temp to all items of İZMİR YUKSEK TEKNOLOJI UNIVERSITY list
      BAKIRÇ_Items=[]  # temp to all items of İZMİR BAKIRÇAY UNIVERSITY list
      DEM_Items=[]  # temp to all items of İZMİR DEMOKRASİ UNIVERSITY list
      İKÇ_Items=[]   # temp to all items of İZMİR KATİP ÇELEBİ  UNIVERSITY list
      res=[]    # Temp to informations of the all universities list
      for d in range(0,13):    # DOKUZ EYÜL UNIVERSITY LOOP      
          uni={"id":program_id[d],"name":program_name[d],"lang":Langu[d],"second":Second[d],"period":Period[d],"spec":Spec[d],
         "quota":Quota[d],"field":Field[d],"last min score":last_score[d],"last min order":last_order[d],"grant":Grant[d]}
          DEU_Items.append(uni)
      deu={"university name":universty_name[0],"uType":uni_typ[0],"items":[{"faculty":faculty[0],"department":DEU_Items}]}         
      res.append(deu)
      for c in range(13,22):    #EGE UNIVERSITY LOOP
          uni={"id":program_id[c],"name":program_name[c],"lang":Langu[c],"second":Second[c],"period":Period[c],"spec":Spec[c],
          "quota":Quota[c],"field":Field[c],"last min score":last_score[c],"last min order":last_order[c],"grant":Grant[c]}
          EU_Items.append(uni)
      eu={"university name":universty_name[1],"uType":uni_typ[1],"items":[{"faculty":faculty[1],"department":EU_Items}]}  
      res.append(eu)
      for i in range(22,50):     #YAŞAR UNIVERSITY LOOP 
          uni={"id":program_id[i],"name":program_name[i],"lang":Langu[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":last_score[i],"last min order":last_order[i],"grant":Grant[i]}
          YAS_Items.append(uni)
      yas={"university name":universty_name[2],"uType":uni_typ[2],"items":[{"faculty":faculty[2],"department":YAS_Items}]}  
      res.append(yas)
      for i in range(50,78):    #İZMİR EKONOMİ UNIVERSITY LOOP  
          uni={"id":program_id[i],"name":program_name[i],"lang":Langu[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":last_score[i],"last min order":last_order[i],"grant":Grant[i]}
          EKO_Items.append(uni)
      eko={"university name":universty_name[3],"uType":uni_typ[3],"items":[{"faculty":faculty[3],"department":EKO_Items}]}  
      res.append(eko)
      for i in range(78,88):     #İZMİR YÜKSEK TEKNOLOJİ UNIVERSITY LOOP 
          uni={"id":program_id[i],"name":program_name[i],"lang":Langu[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":last_score[i],"last min order":last_order[i],"grant":Grant[i]}
          IYTE_Items.append(uni)
      ıyte={"university name":universty_name[4],"uType":uni_typ[4],"items":[{"faculty":faculty[4],"department":IYTE_Items}]}  
      res.append(ıyte)
      for i in range(88,92):     #İZMİR BAKIRÇAY UNIVERSITY LOOP 
          uni={"id":program_id[i],"name":program_name[i],"lang":Langu[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
         "quota":Quota[i],"field":Field[i],"last min score":last_score[i],"last min order":last_order[i],"grant":Grant[i]}
          BAKIRÇ_Items.append(uni)
      bk={"university name":universty_name[5],"uType":uni_typ[5],"items":[{"faculty":faculty[5],"department":BAKIRÇ_Items}]}  
      res.append(bk)
      for i in range(92,97):     # İZMİR DEMOKRASİ UNIVERSITY LOOP 
          uni={"id":program_id[i],"name":program_name[i],"lang":Langu[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":last_score[i],"last min order":last_order[i],"grant":Grant[i]}
          DEM_Items.append(uni)
      dem={"university name":universty_name[6],"uType":uni_typ[6],"items":[{"faculty":faculty[6],"department":DEM_Items}]}  
      res.append(dem)
      for i in range(97,105):     # İZMİR KATİP ÇELEBİ UNIVERSITY LOOP
          uni={"id":program_id[i],"name":program_name[i],"lang":Langu[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
           "quota":Quota[i],"field":Field[i],"last min score":last_score[i],"last min order":last_order[i],"grant":Grant[i]}
          İKÇ_Items.append(uni)
      ikçü={"university name":universty_name[7],"uType":uni_typ[7],"items":[{"faculty":faculty[7],"department":İKÇ_Items}]}  
      res.append(ikçü)
      json.dump(res,Emp_data,ensure_ascii=False,indent=4)   

def type4(input_filename,output_filename):       #JSON FILE TO XML FILE CONVERT METHOD
  uni_name=[]        #temp to university name list 
  uni_type=[]       # temp to universtiy type list 
  faculty=[]        # temp to faculty list 
  program_id=[]      # temp to program id list 
  program_name=[]    # temp to program name list 
  language=[]      # temp to language list
  second=[]       # temp to education type  list 
  period=[]       # temp to education time list 
  spec=[]       # temp to school of degree quota list 
  quota=[]       # temp to quota list 
  field=[]       # temp to score type list 
  last_min_score=[]   # temp to last min score list 
  last_min_order=[]    # temp to last min order list 
  grant=[]            # temp to grant list 
  with open(input_filename) as json_format_file:
    datas=json.load(json_format_file)    # temp to json 
    for temp in datas:      # temp to data root informations 
        uni_name.append(temp['university name'])
        uni_type.append(temp['uType'])
        for items in temp['items']:     # university informations 
            faculty.append(items['faculty'])
            for dep in items['department']:
                program_id.append(dep['id'])
                program_name.append(dep['name'])
                language.append(dep['lang'])
                second.append(dep['second'])
                period.append(dep['period'])
                spec.append(dep['spec'])
                quota.append(dep['quota'])
                field.append(dep['field'])
                last_min_score.append(dep['last min score'])
                last_min_order.append(dep['last min order'])
                grant.append(dep['grant'])
    root=ET.Element("departments")
    k=0  # temp to the loop where ends 
    b=0  # temp to the loop where starts 
    root.text="\n    "
    k=k+12
    for c in range (0,8):
        if k==105:
           k=103
        de=ET.SubElement(root,"university",name=uni_name[c],uType=uni_type[c]) # temp to university name and  type 
        de.tail="\n"
        for i in range(b,k+1):
            if i==105:
                break
            if last_min_score[i] is None:
                last_min_score[i]=''
            if last_min_order[i] is None:
                last_min_order[i]=''
            if language[i] is None:
                language[i]=''
            if spec[i] is None:
                spec[i]=''
            if 'İngilizce'.__eq__(language[i]):
                language[i]='en'             
            tr=ET.SubElement(de,"item",faculty=faculty[c],Id=program_id[i]) # temp to program id and faculty 
            cv=ET.SubElement(tr,"name",lang=language[i],second=second[i])   # temp to language and education type
            pr=ET.SubElement(tr,"period")                                    # temp to education time 
            qt=ET.SubElement(tr,"quota",spec=spec[i])                       # temp unıversity quota 
            fl=ET.SubElement(tr,"field")                                    #temp to score type 
            lm=ET.SubElement(tr,"last_min_score",order=last_min_order[i])    # temp to last min score and order
            gr=ET.SubElement(tr,"grant")                                    # temp to grant 
            lm.text=last_min_score[i] # last sore 
            fl.text=field[i]  # score type 
            qt.text=quota[i]  # quota 
            pr.text=period[i]  # education time 
            cv.text=program_name[i]  # program name 
            gr.text=grant[i]  # grant 
            gr.tail="\n        "           # this parts line break 
            lm.tail="\n            "
            fl.tail="\n            "
            qt.tail="\n            "
            pr.tail="\n            "
            cv.tail="\n            "
            tr.text="\n            "  
            if i==12:                                        # this part loop control for universities start lines and end lines
                b=13
                k=21           
            else:
                tr.tail="\n        "  # for line break( after item ends line  )
            if i==21:
                b=22
                k=49
            else:
                tr.tail="\n        "
            if i==49:
                b=50
                k=77
            else:
                tr.tail="\n        "
            if i==77:
                b=78
                k=87
            else:
                tr.tail="\n        "
            if i==87:
                b=88
                k=91
            else:
                tr.tail="\n        "
            if i==91:
                b=92
                k=96
            else:
                tr.tail="\n        "
            if i==96:
                b=97
                k=104
            else:
                tr.tail="\n        "
            de.tail="\n    "
            de.text="\n        "         
        tr.tail="\n    "    
        if c==7:
              de.tail="\n"
              break           
    tree=ET.ElementTree(root)
    tree.write(output_filename,encoding='utf-8')   

def type5(input_filename,output_filename):      #CSV FILE TO JSON FILE CONVERT METHOD 
  Unitype=[]
  Uniname=[]
  Faclty=[]
  Program_id=[]
  Program_name=[]
  Language=[]
  Second=[]
  Grant=[]
  Period=[]
  Field=[]
  Quota=[]
  Spec=[]
  Order=[]
  Score=[]
  with open (input_filename,'r') as file:
    reader =csv.reader(file,delimiter=';' )
    for row in reader:
        Unitype.append(row[0])
        Uniname.append(row[1])
        Faclty.append(row[2])
        Program_id.append(row[3])
        Program_name.append(row[4])
        if "".__eq__(row[5]):
            row[5]=None
        if 'İngilizce'.__eq__(row[5]):
            row[5]="en"
        Language.append(row[5])
        if "".__eq__(row[6]):
            row[6]="NO"
        Second.append(row[6])
        if "".__eq__(row[7]):
            row[7]=None
        Grant.append(row[7])
        Period.append(row[8])
        Field.append(row[9])
        Quota.append(row[10])
        if "".__eq__(row[11]):
            row[11]=None
        Spec.append(row[11])
        if "".__eq__(row[12]):
            row[12]=None
        Order.append(row[12])
        if "".__eq__(row[13]):
            row[13]=None
        Score.append(row[13]) 
  with open(output_filename,'w',newline='') as Emp_data:
      DEU_Items=[]          # temp to all items of DOKUZ EYLUL UNIVERSITY list
      EU_Items=[]           # temp to all items of EGE UNIVERSITY list
      YAS_Items=[]          # temp to all items of YAŞAR  UNIVERSITY list
      EKO_Items=[]          # temp to all items of İZMİR EKONOMİ UNIVERSITY list
      IYTE_Items=[]         # temp to all items of İZMİR YÜKSEK TEKNOLOJİ UNIVERSITYlist
      BAKIRÇ_Items=[]       # temp to all items of İZMİR BAKIRÇAY UNIVERSITY list
      DEM_Items=[]          # temp to all items of İZMİR DEMOKRASİ UNIVERSITY list
      İKÇ_Items=[]          # temp to all items of İZMİR KATİP ÇELEBİ UNIVERSITY list
      res=[]    # Temp to informations of the all universities list
      for d in range(1,14):        #DOKUZ EYLUL UNIVERSITY 
          uni={"id":Program_id[d],"name":Program_name[d],"lang": Language[d],"second":Second[d],"period":Period[d],"spec":Spec[d],
          "quota":Quota[d],"field":Field[d],"last min score":Score[d],"last min order":Order[d],"grant":Grant[d]}
          DEU_Items.append(uni)
      deu={"university name":Uniname[1],"uType":Unitype[1],"items":[{"faculty":Faclty[1],"department":DEU_Items}]}         
      res.append(deu)
      for c in range(14,23):     #EGE UNIVERSITY 
          uni={"id":Program_id[c],"name":Program_name[c],"lang": Language[c],"second":Second[c],"period":Period[c],"spec":Spec[c],
           "quota":Quota[c],"field":Field[c],"last min score":Score[c],"last min order":Order[c],"grant":Grant[c]}
          EU_Items.append(uni)
      eu={"university name":Uniname[14],"uType":Unitype[14],"items":[{"faculty":Faclty[14],"department":EU_Items}]}  
      res.append(eu)
      for i in range(23,51):     #YAŞAR UNIVERSITY 
          uni={"id":Program_id[i],"name":Program_name[i],"lang": Language[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":Score[i],"last min order":Order[i],"grant":Grant[i]}
          YAS_Items.append(uni)
      yas={"university name":Uniname[23],"uType":Unitype[23],"items":[{"faculty":Faclty[23],"department":YAS_Items}]}  
      res.append(yas)
      for i in range(51,79):     #İZMİR EKONOMİ UNIVERSITY
          uni={"id":Program_id[i],"name":Program_name[i],"lang": Language[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":Score[i],"last min order":Order[i],"grant":Grant[i]}
          EKO_Items.append(uni)
      eko={"university name":Uniname[51],"uType":Unitype[51],"items":[{"faculty":Faclty[51],"department":EKO_Items}]}  
      res.append(eko)
      for i in range(79,89):     #İZMİR YÜKSEK TEKNOLOJİ UNIVERSITY
          uni={"id":Program_id[i],"name":Program_name[i],"lang": Language[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":Score[i],"last min order":Order[i],"grant":Grant[i]}
          IYTE_Items.append(uni)
      ıyte={"university name":Uniname[79],"uType":Unitype[79],"items":[{"faculty":Faclty[79],"department":IYTE_Items}]}  
      res.append(ıyte)
      for i in range(89,93):     #İZMİR BAKIRÇAY UNIVERSITY
          uni={"id":Program_id[i],"name":Program_name[i],"lang": Language[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":Score[i],"last min order":Order[i],"grant":Grant[i]}
          BAKIRÇ_Items.append(uni)
      bk={"university name":Uniname[89],"uType":Unitype[89],"items":[{"faculty":Faclty[89],"department":BAKIRÇ_Items}]}  
      res.append(bk)
      for i in range(93,98):     #İZMİR DEMOKRASİ UNIVERSITY
          uni={"id":Program_id[i],"name":Program_name[i],"lang": Language[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":Score[i],"last min order":Order[i],"grant":Grant[i]}
          DEM_Items.append(uni)
      dem={"university name":Uniname[93],"uType":Unitype[93],"items":[{"faculty":Faclty[93],"department":DEM_Items}]}  
      res.append(dem)
      for i in range(98,106):     #İZMİR KATİP ÇELEBİ UNIVERSITY
          uni={"id":Program_id[i],"name":Program_name[i],"lang": Language[i],"second":Second[i],"period":Period[i],"spec":Spec[i],
          "quota":Quota[i],"field":Field[i],"last min score":Score[i],"last min order":Order[i],"grant":Grant[i]}
          İKÇ_Items.append(uni)
      ikçü={"university name":Uniname[98],"uType":Unitype[98],"items":[{"faculty":Faclty[98],"department":İKÇ_Items}]}  
      res.append(ikçü)
      json.dump(res,Emp_data,ensure_ascii=False,indent=4)  #write to json file

def type6(input_filename,output_filename):          #CSV FILE TO JSON FILE CONVERT METHOD 
  with open(input_filename) as json_format_file:
    datas=json.load(json_format_file)
  with open (output_filename,'w',newline='') as Emp_data:
    csvwriter=csv.writer(Emp_data,delimiter=";")
    Emp_data.write("University Type,University Name,Faculty,Program Id,Program,Language,Education Type,Qrant,Education Time,Field,Quota,School Degree Quota,Last Min Score Order,Last Min Score\n")
    for temp in datas:
        emp_nodes=[]  
        for items in temp['items']:
            for dep in items['department']:      
                emp_nodes.append(temp['uType'])
                emp_nodes.append(temp['university name'])
                emp_nodes.append(items['faculty'])
                emp_nodes.append(dep['id'])
                emp_nodes.append(dep['name'])
                if 'en'.__eq__(dep['lang']):
                    dep['lang']="İngilizce"      
                emp_nodes.append(dep['lang'])
                if 'NO'.__eq__(dep['second']):
                      dep['second']=''
                emp_nodes.append(dep['second'])
                emp_nodes.append(dep['grant'])
                emp_nodes.append(dep['period'])
                emp_nodes.append(dep['field'])
                emp_nodes.append(dep['quota'])
                emp_nodes.append(dep['spec'])
                emp_nodes.append(dep['last min order'])
                emp_nodes.append((dep['last min score']))        
                csvwriter.writerow(emp_nodes) 
                emp_nodes.clear()  

def type7(input_filename,output_filename):        #XML VALIDATES WITH XSD METHOD 
    doc = etree.parse(input_filename)      #temp to xml file name 
    root = doc.getroot()                   # temp to xml file root 
    xmlschema_doc = etree.parse(output_filename)    # temp to xsd 
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.XML(etree.tostring(root))
    validation_result = xmlschema.validate(doc)
    print(validation_result)

if  __name__ == "__main__":         # MAIN METHOD (ARGUMENT FROM USER )  # write to the command line : python 2017510067.py inputfilename outputfilename type
      inpfile=sys.argv[1]
      outpfile=sys.argv[2]
      if sys.argv[3].__eq__('type1'):   # csv to xml 
            type1(inpfile,outpfile)
      if sys.argv[3].__eq__('type2'):   #xml to csv
            type2(inpfile,outpfile)
      if sys.argv[3].__eq__('type3'):   # xml to json 
            type3(inpfile,outpfile)   
      if sys.argv[3].__eq__('type4'):  #json to xml 
            type4(inpfile,outpfile)
      if sys.argv[3].__eq__('type5'):  #csv to json
            type5(inpfile,outpfile)
      if sys.argv[3].__eq__('type6'):  #json to csv 
            type6(inpfile,outpfile)
      if sys.argv[3].__eq__('type7'):  #xml validates with xsd 
            type7(inpfile,outpfile)
                  