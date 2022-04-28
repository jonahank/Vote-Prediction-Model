import re

def load_speaker_fix_dict(py27 = False):
    
    if py27:
        # clean names by removing titles
        replace_dict = {'Tredje næstformand':'', 'Anden næstformand':'', 'Skatteministeren':'',
                       'Miljøministeren':'', 'Fødevareministeren':'', 'Statsministeren':'', 'Kirkeministeren':'',
                       'Uddannelses- og forskningsministeren':'', 'Ministeren for sundhed og forebyggelse':'','og kirke':'',
                       'Erhvervs- og vækstministeren':'', 'Undervisningsministeren':'', 'Udenrigsministeren':'',
                       'Den fg. formand':'', 'Forsvarsministeren':'', 'Fjerde næstformand':'', 'Formanden':'',
                       'Handels- og udviklingsministeren': '', 'Transportministeren':'','Udviklingsministeren':'',
                       'Aldersformanden (Bertel Haarder)':'','Aldersformanden':'','Ministeren for ligestilling og kirke':'',
                       'Ministeren for børn, ligestilling, integration og sociale forhold':'','Kulturministeren':'',
                       'Ministeren for by, bolig og landdistrikter':'', 'Ministeren for nordisk samarbejde':'',
                       'Justitsministeren':'', 'Økonomi- og indenrigsministeren':'', 'Finansministeren':'',
                       'Første næstformand':'', 'Beskæftigelsesministeren':'','Ældreministeren':'',
                       'Klima-, energi- og bygningsministeren':'', 'Miljø- og fødevareministeren':'',
                       'Udlændinge-, integrations- og boligministeren':'', 'Social- og indenrigsministeren':'',
                       'Miljø- og fødevareministeren':'','Sundheds- og ældreministeren':'',
                       'Ministeren for børn, undervisning og ligestilling':'','Transport- og bygningsministeren':'', 
                       'Energi-, forsynings- og klimaministeren':'','Børne- og socialministeren':'',
                       'Sundhedsministeren':'','Ministeren for offentlig innovation':'','Erhvervsministeren':'',
                       'Transport-, bygnings- og boligministeren':'','Udlændinge- og integrationsministeren':'',
                       'Ministeren for ligestilling':'','Ministeren for udviklingssamarbejde':'',
                       'Ministeren for fiskeri og ligestilling':'','Social-, børne- og integrationsministeren':'',
                       'Ministeren for forskning, innovation og videregående uddannelser':'',
                       'Handels- og europaministeren':'','Ministeren for fødevarer, fiskeri og ligestilling':'',
                       'Boligministeren':'','Børne- og undervisningsministeren':'',
                        'Klima-, energi- og forsyningsministeren':'','Beskæftigelsesminister og minister for ligestilling':'',


                    # also fix other strange things in data
                       '(Bertel Haarder) Bertel Haarder': 'Bertel Haarder (V)',
                       'Hans Christian Schmidt Hans Christian Schmidt':'Hans Christian Schmidt (V)',
                       'Karen Ellemann Karen Ellemann':'Karen Ellemann (V)',
                       'Peter Christensen Peter Christensen':'Peter Christensen (V)', 
                       'Karsten Lauritzen Karsten Lauritzen':'Karsten Lauritzen (V)',
                       'Kristian Jensen Kristian Jensen':'Kristian Jensen (V)',
                       'Søren Pape Poulsen Søren Pape Poulsen':'Søren Pape Poulsen (KF)',
                       'Ole Birk Olesen Ole Birk Olesen':'Ole Birk Olesen (LA)',
                       'Eva Kjer Hansen Eva Kjer Hansen':'Eva Kjer Hansen (V)',
                       'Morten Østergaard Morten Østergaard':'Morten Østergaard (RV)',
                       'Nick Hækkerup Nick Hækkerup':'Nick Hækkerup (S)',
                       'Rasmus Helveg Petersen Rasmus Helveg Petersen':'Rasmus Helveg Petersen (RV)',
                       'Benny Engelbrecht Benny Engelbrecht':'Benny Engelbrecht','Rasmus Prehn Rasmus Prehn':'Rasmus Prehn',
                       'Mette Frederiksen Mette Frederiksen':'Mette Frederiksen','Mogens Jensen Mogens Jensen':'Mogens Jensen',
                       'Morten Bødskov Morten Bødskov':'Morten Bødskov'}

    else:
        replace_dict = {'Tredje næstformand':'', 'Anden næstformand':'', 'Skatteministeren':'',
                       'Miljøministeren':'', 'Fødevareministeren':'', 'Statsministeren':'', 'Kirkeministeren':'',
                       'Uddannelses- og forskningsministeren':'', 'Ministeren for sundhed og forebyggelse':'','og kirke':'',
                       'Erhvervs- og vækstministeren':'', 'Undervisningsministeren':'', 'Udenrigsministeren':'',
                       'Den fg. formand':'', 'Forsvarsministeren':'', 'Fjerde næstformand':'', 'Formanden':'',
                       'Handels- og udviklingsministeren': '', 'Transportministeren':'','Udviklingsministeren':'',
                       'Aldersformanden (Bertel Haarder)':'','Aldersformanden':'','Ministeren for ligestilling og kirke':'',
                       'Ministeren for børn, ligestilling, integration og sociale forhold':'','Kulturministeren':'',
                       'Ministeren for by, bolig og landdistrikter':'', 'Ministeren for nordisk samarbejde':'',
                       'Justitsministeren':'', 'Økonomi- og indenrigsministeren':'', 'Finansministeren':'',
                       'Første næstformand':'', 'Beskæftigelsesministeren':'','Ældreministeren':'',
                       'Klima-, energi- og bygningsministeren':'', 'Miljø- og fødevareministeren':'',
                       'Udlændinge-, integrations- og boligministeren':'', 'Social- og indenrigsministeren':'',
                       'Miljø- og fødevareministeren':'','Sundheds- og ældreministeren':'',
                       'Ministeren for børn, undervisning og ligestilling':'','Transport- og bygningsministeren':'', 
                       'Energi-, forsynings- og klimaministeren':'','Børne- og socialministeren':'',
                       'Sundhedsministeren':'','Ministeren for offentlig innovation':'','Erhvervsministeren':'',
                       'Transport-, bygnings- og boligministeren':'','Udlændinge- og integrationsministeren':'',
                       'Ministeren for ligestilling':'','Ministeren for udviklingssamarbejde':'',
                       'Ministeren for fiskeri og ligestilling':'','Social-, børne- og integrationsministeren':'',
                       'Ministeren for forskning, innovation og videregående uddannelser':'',
                       'Handels- og europaministeren':'','Ministeren for fødevarer, fiskeri og ligestilling':'',
                       'Boligministeren':'','Børne- og undervisningsministeren':'',
                        'Klima-, energi- og forsyningsministeren':'','Ministeren for fødevarer, landbrug og fiskeri':'',
                        'Beskæftigelsesminister og minister for ligestilling':'',

                    # also fix other strange things in data
                       '(Bertel Haarder) Bertel Haarder': 'Bertel Haarder (V)',
                       'Hans Christian Schmidt Hans Christian Schmidt':'Hans Christian Schmidt (V)',
                       'Karen Ellemann Karen Ellemann':'Karen Ellemann (V)',
                       'Peter Christensen Peter Christensen':'Peter Christensen (V)', 
                       'Karsten Lauritzen Karsten Lauritzen':'Karsten Lauritzen (V)',
                       'Kristian Jensen Kristian Jensen':'Kristian Jensen (V)',
                       'Søren Pape Poulsen Søren Pape Poulsen':'Søren Pape Poulsen (KF)',
                       'Ole Birk Olesen Ole Birk Olesen':'Ole Birk Olesen (LA)',
                       'Eva Kjer Hansen Eva Kjer Hansen':'Eva Kjer Hansen (V)',
                       'Morten Østergaard Morten Østergaard':'Morten Østergaard (RV)',
                       'Nick Hækkerup Nick Hækkerup':'Nick Hækkerup (S)',
                       'Rasmus Helveg Petersen Rasmus Helveg Petersen':'Rasmus Helveg Petersen (RV)',
                       'Benny Engelbrecht Benny Engelbrecht':'Benny Engelbrecht','Rasmus Prehn Rasmus Prehn':'Rasmus Prehn',
                       'Mette Frederiksen Mette Frederiksen':'Mette Frederiksen','Mogens Jensen Mogens Jensen':'Mogens Jensen',
                       'Morten Bødskov Morten Bødskov':'Morten Bødskov'}

    rep = dict((re.escape(k), v) for k, v in replace_dict.items())
    pattern = re.compile("|".join(rep.keys()))

    return pattern, rep

def load_fix_party_affiliations():
    
    # people who were ministers do not have party affiliation in the data
    # and some people have missing party affiliations (errors in the data)
    # to fix this manually constructed this mapping, to be used only if people no explicit party affiliation exist in data
    fix_aff = {
               'Alex Ahrendtsen':'(DF)',
               'Ane Halsboe-Jørgensen':'(S)',
               'Anders Samuelsen':'(LA)',
               'Anne Baastrup':'(SF)',
               'Annette Lind':'(S)',
               'Annette Vilhelmsen':'(SF)',
               'Astrid Krag':'(SF)', # was SF while she was a minister, later switched to S - correctly captured in data
               'Benny Engelbrecht':'(S)',
               'Bent Bøgsted':'(DF)',
               'Bertel Haarder':'(V)',
               'Bjarne Corydon':'(S)',
               'Brian Mikkelsen':'(KF)',
               'Camilla Hersom':'(RV)',
               'Carsten Hansen':'(S)',
               'Christian Friis Bach':'(RV)',
               'Christian Juhl':'(EL)',
               'Christine Antorini':'(S)',
               'Claus Hjort Frederiksen':'(V)',
               'Dan Jørgensen':'(S)',
               'Ellen Trane Nørby':'(V)',
               'Erling Bonnesen':'(V)',
               'Esben Lunde Larsen':'(V)',
               'Eva Kjer Hansen':'(V)',
               'Flemming Møller Mortensen':'(S)',
               'Hans Christian Schmidt':'(V)',
               'Helle Thorning-Schmidt':'(S)',
               'Henrik Dam Kristensen':'(S)',
               'Henrik Sass Larsen':'(S)',
               'Holger K. Nielsen':'(SF)',
               'Ida Auken':'(SF)', # was SF while she was a minister, later switched to RV - correctly captured in data
               'Inger Støjberg':'(V)',
               'Jakob Ellemann-Jensen':'(V)',
               'Jens Rohde': '(RV)',
               'Jeppe Kofod':'(S)',
               'John Dyrby Paulsen':'(S)',
               'Jonas Dahl':'(SF)',
               'Joy Mogensen':'(S)',
               'Jørn Neergaard Larsen':'(V)',
               'Kaare Dybvad':'(S)',
               'Kaare Dybvad Bek':'(S)',
               'Karen Ellemann':'(V)',
               'Karen Hækkerup':'(S)',
               'Karen J. Klint':'(S)',
               'Karsten Lauritzen':'(V)',
               'Kirsten Brosbøl':'(S)',
               'Kristian Jensen':'(V)',
               'Kristian Pihl Lorentzen':'(V)',
               'Lars Christian Lilleholt':'(V)',
               'Lars Løkke Rasmussen':'(V)',
               'Lea Wermelin':'(S)',
               'Leif Mikkelsen':'(LA)',
               'Lone Loklindt':'(RV)',
               'Magnus Heunicke':'(S)',
               'Mai Mercado':'(KF)',
               'Manu Sareen':'(RV)',
               'Margrethe Vestager':'(RV)',
               'Marianne Jelved':'(RV)',
               'Martin Lidegaard':'(RV)',
               'Mattias Tesfaye':'(S)',
               'Merete Riisager':'(LA)',
               'Mette Bock':'(LA)',
               'Mette Frederiksen':'(S)',
               'Mogens Jensen':'(S)',
               'Mogens Lykketoft':'(S)',
               'Morten Bødskov':'(S)',
               'Morten Østergaard':'(RV)',
               'Nick Hækkerup':'(S)',
               'Nicolai Wammen':'(S)',
               'Ole Birk Olesen':'(LA)',
               'Per Clausen':'(EL)',
               'Pernille Rosenkrantz-Theil':'(S)',
               'Peter Christensen':'(V)',
               'Peter Hummelgaard Thomsen':'(S)',
               'Peter Hummelgaard': '(S)',
               'Pia Kjærsgaard':'(DF)',
               'Pia Olsen Dyhr':'(SF)',
               'Rasmus Helveg Petersen':'(RV)',
               'Rasmus Jarlov':'(KF)',
               'Rasmus Prehn':'(S)',
               'Simon Emil Ammitzbøll-Bille':'(LA)',
               'Simon Emil Ammitzbøll':'(LA)',
               'Simon Kollerup':'(S)',
               'Sofie Carsten Nielsen':'(RV)',
               'Sophie Løhde':'(V)',
               'Steen Gade':'(SF)',
               'Stine Brix':'(EL)',
               'Søren Pape Poulsen':'(KF)',
               'Søren Pind':'(V)',
               'Thyra Frank':'(LA)',
               'Tommy Ahlers':'(V)',
               'Trine Bramsen':'(S)',
               'Trine Torp': '(SF)',
               'Troels Lund Poulsen':'(V)',
               'Ulla Tørnæs':'(V)'
              }
    return fix_aff

def load_party_numbers(y,m,d):
    t = datetime(y,m,d)

    if t < datetime(2015,2,4):
        return {'V':47,'S':44,'DF':22,'RV':17,'SF':16,'EL':12,'LA':9,'KF':8,'OTH':4}

    elif dattime(2015,2,4) <= t < datetime(2015,6,18):
        # SF left the government on Feb 3rd
        # Ida Auken left SF and joined RV
        # Astrid Krag left SF and joined S
        return {'V':47,'S':45,'DF':22,'RV':18,'SF':14,'EL':12,'LA':9,'KF':8,'OTH':4}

    elif datetime(2015,6,19) <= t < datetime(2019,6,5):
        return {'S':47,'DF':37,'V':34,'EL':14,'LA':13,'RV':8,'SF':7,'KF':6,'OTH':13}

    elif datetime(2019,6,5) <= t:
        return {'S':48,'V':43,'DF':16,'RV':16,'SF':14,'EL':13,'KF':12,'LA':4,'OTH':17}





    
    