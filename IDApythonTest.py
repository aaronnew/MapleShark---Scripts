from idaapi import *  
from idc import *  
import math


def gethexind(buffstat, firstStr):
    Y = (math.log(buffstat) / math.log(2));
    return (31 - Y) + (firstStr * 32)

def ShowFlags(Flag):
    if (GetFlags(Flag)!= 0 ):
        iii=0;
        val=0;
        while (iii<17):
            val=Dword(Flag+iii*4);
            if(val!=0):
                #print ("pos=%d; hex = %#x  st=%d; \n"%(iii, val,gethexind(val,iii)));
                print(" map.put(%#x,%d); "%(Flag, gethexind(val,iii)));
            iii=iii+1;
    else:
        print("无数据");
# for i in range(0, 9):
#     ShowFlags(68 * i + 0x22B8218)
ShowFlags(0x22408F8);
ShowFlags(0x22408F8);
ShowFlags(0x2240940);
ShowFlags(0x2240940);
ShowFlags(0x2240988);
ShowFlags(0x2240988);
ShowFlags(0x22409D0);
ShowFlags(0x22409D0);
ShowFlags(0x2240A18);
ShowFlags(0x2240A18);
ShowFlags(0x2240A60);
ShowFlags(0x2240A60);
ShowFlags(0x2240AA8);
ShowFlags(0x2240AA8);
ShowFlags(0x2240AF0);
ShowFlags(0x2240AF0);
ShowFlags(0x2240B38);
ShowFlags(0x2240B38);
ShowFlags(0x2240B80);
ShowFlags(0x2240B80);
ShowFlags(0x2240BC8);
ShowFlags(0x2240BC8);
ShowFlags(0x2240C10);
ShowFlags(0x2240C10);
ShowFlags(0x2240C58);
ShowFlags(0x2240C58);
ShowFlags(0x2240CA0);
ShowFlags(0x2240CA0);
ShowFlags(0x2240CE8);
ShowFlags(0x2240CE8);
ShowFlags(0x2240D30);
ShowFlags(0x2240D30);
ShowFlags(0x2240D78);
ShowFlags(0x2240D78);
ShowFlags(0x2240DC0);
ShowFlags(0x2240DC0);
ShowFlags(0x2240E08);
ShowFlags(0x2240E08);
ShowFlags(0x2240E50);
ShowFlags(0x2240E50);
ShowFlags(0x2240E98);
ShowFlags(0x2240E98);
ShowFlags(0x2240EE0);
ShowFlags(0x2240EE0);
ShowFlags(0x2240F28);
ShowFlags(0x2240F28);
ShowFlags(0x2240F70);
ShowFlags(0x2240F70);
ShowFlags(0x2240FB8);
ShowFlags(0x2240FB8);
ShowFlags(0x2241000);
ShowFlags(0x2241000);
ShowFlags(0x2241048);
ShowFlags(0x2241048);
ShowFlags(0x2241090);
ShowFlags(0x2241090);
ShowFlags(0x22410D8);
ShowFlags(0x22410D8);
ShowFlags(0x2241120);
ShowFlags(0x2241120);
ShowFlags(0x2241168);
ShowFlags(0x2241168);
ShowFlags(0x22411B0);
ShowFlags(0x22411B0);
ShowFlags(0x22411F8);
ShowFlags(0x22411F8);
ShowFlags(0x2241240);
ShowFlags(0x2241240);
ShowFlags(0x2241288);
ShowFlags(0x2241288);
ShowFlags(0x22412D0);
ShowFlags(0x22412D0);
ShowFlags(0x2241318);
ShowFlags(0x2241318);
ShowFlags(0x2241360);
ShowFlags(0x2241360);
ShowFlags(0x22413A8);
ShowFlags(0x22413A8);
ShowFlags(0x2240598);
ShowFlags(0x2240598);
ShowFlags(0x22413F0);
ShowFlags(0x22413F0);
ShowFlags(0x2241438);
ShowFlags(0x2241438);
ShowFlags(0x2241480);
ShowFlags(0x2241480);
ShowFlags(0x22414C8);
ShowFlags(0x22414C8);
ShowFlags(0x2241510);
ShowFlags(0x2241510);
ShowFlags(0x2241558);
ShowFlags(0x2241558);
ShowFlags(0x22415A0);
ShowFlags(0x22415A0);
ShowFlags(0x22415E8);
ShowFlags(0x22415E8);
ShowFlags(0x2241630);
ShowFlags(0x2241630);
ShowFlags(0x2241678);
ShowFlags(0x2241678);
ShowFlags(0x22416C0);
ShowFlags(0x22416C0);
ShowFlags(0x2241708);
ShowFlags(0x2241708);
ShowFlags(0x2241750);
ShowFlags(0x2241750);
ShowFlags(0x2241798);
ShowFlags(0x2241798);
ShowFlags(0x22417E0);
ShowFlags(0x22417E0);
ShowFlags(0x2241828);
ShowFlags(0x2241828);
ShowFlags(0x2241870);
ShowFlags(0x2241870);
ShowFlags(0x22418B8);
ShowFlags(0x22418B8);
ShowFlags(0x2241900);
ShowFlags(0x2241900);
ShowFlags(0x2241948);
ShowFlags(0x2241948);
ShowFlags(0x2241990);
ShowFlags(0x2241990);
ShowFlags(0x22408B0);
ShowFlags(0x22408B0);
ShowFlags(0x22419D8);
ShowFlags(0x22419D8);
ShowFlags(0x2241A20);
ShowFlags(0x2241A20);
ShowFlags(0x2241A68);
ShowFlags(0x2241A68);
ShowFlags(0x2241AB0);
ShowFlags(0x2241AB0);
ShowFlags(0x2241AF8);
ShowFlags(0x2241AF8);
ShowFlags(0x2241B40);
ShowFlags(0x2241B40);
ShowFlags(0x2241B88);
ShowFlags(0x2241B88);
ShowFlags(0x2241BD0);
ShowFlags(0x2241BD0);
ShowFlags(0x2241C18);
ShowFlags(0x2241C18);
ShowFlags(0x2241C60);
ShowFlags(0x2241C60);
ShowFlags(0x2241CA8);
ShowFlags(0x2241CA8);
ShowFlags(0x2241CF0);
ShowFlags(0x2241CF0);
ShowFlags(0x2241D38);
ShowFlags(0x2241D38);
ShowFlags(0x2241D80);
ShowFlags(0x2241D80);
ShowFlags(0x2241DC8);
ShowFlags(0x2241DC8);
ShowFlags(0x2241E10);
ShowFlags(0x2241E10);
ShowFlags(0x2241E58);
ShowFlags(0x2241E58);
ShowFlags(0x2241EA0);
ShowFlags(0x2241EA0);
ShowFlags(0x2241EE8);
ShowFlags(0x2241EE8);
ShowFlags(0x2241F30);
ShowFlags(0x2241F30);
ShowFlags(0x2241F78);
ShowFlags(0x2241F78);
ShowFlags(0x2241FC0);
ShowFlags(0x2241FC0);
ShowFlags(0x2242008);
ShowFlags(0x2242008);
ShowFlags(0x2242050);
ShowFlags(0x2242050);
ShowFlags(0x2242098);
ShowFlags(0x2242098);
ShowFlags(0x22420E0);
ShowFlags(0x22420E0);
ShowFlags(0x2242128);
ShowFlags(0x2242128);
ShowFlags(0x2242170);
ShowFlags(0x2242170);
ShowFlags(0x22421B8);
ShowFlags(0x22421B8);
ShowFlags(0x2242200);
ShowFlags(0x2242200);
ShowFlags(0x2242248);
ShowFlags(0x2242248);
ShowFlags(0x2242290);
ShowFlags(0x2242290);
ShowFlags(0x22422D8);
ShowFlags(0x22422D8);
ShowFlags(0x2242320);
ShowFlags(0x2242320);
ShowFlags(0x2242368);
ShowFlags(0x2242368);
ShowFlags(0x22423B0);
ShowFlags(0x22423B0);
ShowFlags(0x22423F8);
ShowFlags(0x22423F8);
ShowFlags(0x2242440);
ShowFlags(0x2242440);
ShowFlags(0x2242488);
ShowFlags(0x2242488);
ShowFlags(0x22424D0);
ShowFlags(0x22424D0);
ShowFlags(0x2242518);
ShowFlags(0x2242518);
ShowFlags(0x2240790);
ShowFlags(0x2240790);
ShowFlags(0x2242560);
ShowFlags(0x2242560);
ShowFlags(0x22425A8);
ShowFlags(0x22425A8);
ShowFlags(0x22425F0);
ShowFlags(0x22425F0);
ShowFlags(0x2242638);
ShowFlags(0x2242638);
ShowFlags(0x2242680);
ShowFlags(0x2242680);
ShowFlags(0x22426C8);
ShowFlags(0x22426C8);
ShowFlags(0x2242710);
ShowFlags(0x2242710);
ShowFlags(0x2242758);
ShowFlags(0x2242758);
ShowFlags(0x22407D8);
ShowFlags(0x22407D8);
ShowFlags(0x22427A0);
ShowFlags(0x22427A0);
ShowFlags(0x22427E8);
ShowFlags(0x22427E8);
ShowFlags(0x2242830);
ShowFlags(0x2242830);
ShowFlags(0x2242878);
ShowFlags(0x2242878);
ShowFlags(0x22428C0);
ShowFlags(0x22428C0);
ShowFlags(0x2242908);
ShowFlags(0x2242908);
ShowFlags(0x2242950);
ShowFlags(0x2242950);
ShowFlags(0x2242998);
ShowFlags(0x2242998);
ShowFlags(0x22429E0);
ShowFlags(0x22429E0);
ShowFlags(0x2242A28);
ShowFlags(0x2242A28);
ShowFlags(0x2242A70);
ShowFlags(0x2242A70);
ShowFlags(0x2242AB8);
ShowFlags(0x2242AB8);
ShowFlags(0x2242B00);
ShowFlags(0x2242B00);
ShowFlags(0x2242B48);
ShowFlags(0x2242B48);
ShowFlags(0x2242B90);
ShowFlags(0x2242B90);
ShowFlags(0x2242BD8);
ShowFlags(0x2242BD8);
ShowFlags(0x2242C20);
ShowFlags(0x2242C20);
ShowFlags(0x2242C68);
ShowFlags(0x2242C68);
ShowFlags(0x2242CB0);
ShowFlags(0x2242CB0);
ShowFlags(0x2242CF8);
ShowFlags(0x2242CF8);
ShowFlags(0x2242D40);
ShowFlags(0x2242D40);
ShowFlags(0x2242D88);
ShowFlags(0x2242D88);
ShowFlags(0x2242DD0);
ShowFlags(0x2242DD0);
ShowFlags(0x2242E18);
ShowFlags(0x2242E18);
ShowFlags(0x2242E60);
ShowFlags(0x2242E60);
ShowFlags(0x2242EA8);
ShowFlags(0x2242EA8);
ShowFlags(0x2242EF0);
ShowFlags(0x2242EF0);
ShowFlags(0x2242F38);
ShowFlags(0x2242F38);
ShowFlags(0x2242F80);
ShowFlags(0x2242F80);
ShowFlags(0x2242FC8);
ShowFlags(0x2242FC8);
ShowFlags(0x2243010);
ShowFlags(0x2243010);
ShowFlags(0x2243058);
ShowFlags(0x2243058);
ShowFlags(0x22430A0);
ShowFlags(0x22430A0);
ShowFlags(0x22430E8);
ShowFlags(0x22430E8);
ShowFlags(0x2243130);
ShowFlags(0x2243130);
ShowFlags(0x2243178);
ShowFlags(0x2243178);
ShowFlags(0x22431C0);
ShowFlags(0x22431C0);
ShowFlags(0x2243208);
ShowFlags(0x2243208);
ShowFlags(0x2243250);
ShowFlags(0x2243250);
ShowFlags(0x2243298);
ShowFlags(0x2243298);
ShowFlags(0x22432E0);
ShowFlags(0x22432E0);
ShowFlags(0x2243328);
ShowFlags(0x2243328);
ShowFlags(0x2243370);
ShowFlags(0x2243370);
ShowFlags(0x22433B8);
ShowFlags(0x22433B8);
ShowFlags(0x2243400);
ShowFlags(0x2243400);
ShowFlags(0x2243448);
ShowFlags(0x2243448);
ShowFlags(0x2240430);
ShowFlags(0x2240430);
ShowFlags(0x2243490);
ShowFlags(0x2243490);
ShowFlags(0x22434D8);
ShowFlags(0x22434D8);
ShowFlags(0x2243520);
ShowFlags(0x2243520);
ShowFlags(0x2243568);
ShowFlags(0x2243568);
ShowFlags(0x22435B0);
ShowFlags(0x22435B0);
ShowFlags(0x22435F8);
ShowFlags(0x22435F8);
ShowFlags(0x2243640);
ShowFlags(0x2243640);
ShowFlags(0x2243688);
ShowFlags(0x2243688);
ShowFlags(0x22436D0);
ShowFlags(0x22436D0);
ShowFlags(0x2243718);
ShowFlags(0x2243718);
ShowFlags(0x2243760);
ShowFlags(0x2243760);
ShowFlags(0x22437A8);
ShowFlags(0x22437A8);
ShowFlags(0x22437F0);
ShowFlags(0x22437F0);
ShowFlags(0x2243838);
ShowFlags(0x2243838);
ShowFlags(0x2243880);
ShowFlags(0x2243880);
ShowFlags(0x22438C8);
ShowFlags(0x22438C8);
ShowFlags(0x2243910);
ShowFlags(0x2243910);
ShowFlags(0x2243958);
ShowFlags(0x2243958);
ShowFlags(0x22439A0);
ShowFlags(0x22439A0);
ShowFlags(0x22439E8);
ShowFlags(0x22439E8);
ShowFlags(0x2243A30);
ShowFlags(0x2243A30);
ShowFlags(0x22403E8);
ShowFlags(0x22403E8);
ShowFlags(0x2243A78);
ShowFlags(0x2243A78);
ShowFlags(0x2243AC0);
ShowFlags(0x2243AC0);
ShowFlags(0x2243B08);
ShowFlags(0x2243B08);
ShowFlags(0x2243B50);
ShowFlags(0x2243B50);
ShowFlags(0x2243B98);
ShowFlags(0x2243B98);
ShowFlags(0x2243BE0);
ShowFlags(0x2243BE0);
ShowFlags(0x2243C28);
ShowFlags(0x2243C28);
ShowFlags(0x2243C70);
ShowFlags(0x2243C70);
ShowFlags(0x2243CB8);
ShowFlags(0x2243CB8);
ShowFlags(0x2243D00);
ShowFlags(0x2243D00);
ShowFlags(0x2243D48);
ShowFlags(0x2243D48);
ShowFlags(0x2243D90);
ShowFlags(0x2243D90);
ShowFlags(0x2243DD8);
ShowFlags(0x2243DD8);
ShowFlags(0x2243E20);
ShowFlags(0x2243E20);
ShowFlags(0x2243E68);
ShowFlags(0x2243E68);
ShowFlags(0x2243EB0);
ShowFlags(0x2243EB0);
ShowFlags(0x2240478);
ShowFlags(0x2240478);
ShowFlags(0x2243EF8);
ShowFlags(0x2243EF8);
ShowFlags(0x2243F40);
ShowFlags(0x2243F40);
ShowFlags(0x2243F88);
ShowFlags(0x2243F88);
ShowFlags(0x2243FD0);
ShowFlags(0x2243FD0);
ShowFlags(0x2244018);
ShowFlags(0x2244018);
ShowFlags(0x2244060);
ShowFlags(0x2244060);
ShowFlags(0x22440A8);
ShowFlags(0x22440A8);
ShowFlags(0x22404C0);
ShowFlags(0x22404C0);
ShowFlags(0x22440F0);
ShowFlags(0x22440F0);
ShowFlags(0x2240508);
ShowFlags(0x2240508);
ShowFlags(0x2244138);
ShowFlags(0x2244138);
ShowFlags(0x2244180);
ShowFlags(0x2244180);
ShowFlags(0x22441C8);
ShowFlags(0x22441C8);
ShowFlags(0x2244210);
ShowFlags(0x2244210);
ShowFlags(0x2244258);
ShowFlags(0x2244258);
ShowFlags(0x22442A0);
ShowFlags(0x22442A0);
ShowFlags(0x22442E8);
ShowFlags(0x22442E8);
ShowFlags(0x2244330);
ShowFlags(0x2244330);
ShowFlags(0x2244378);
ShowFlags(0x2244378);
ShowFlags(0x22443C0);
ShowFlags(0x22443C0);
ShowFlags(0x2244408);
ShowFlags(0x2244408);
ShowFlags(0x2244450);
ShowFlags(0x2244450);
ShowFlags(0x2244498);
ShowFlags(0x2244498);
ShowFlags(0x22444E0);
ShowFlags(0x22444E0);
ShowFlags(0x2244528);
ShowFlags(0x2244528);
ShowFlags(0x2244570);
ShowFlags(0x2244570);
ShowFlags(0x22445B8);
ShowFlags(0x22445B8);
ShowFlags(0x2244600);
ShowFlags(0x2244600);
ShowFlags(0x2244648);
ShowFlags(0x2244648);
ShowFlags(0x2244690);
ShowFlags(0x2244690);
ShowFlags(0x22446D8);
ShowFlags(0x22446D8);
ShowFlags(0x2244720);
ShowFlags(0x2244720);
ShowFlags(0x2244768);
ShowFlags(0x2244768);
ShowFlags(0x22447B0);
ShowFlags(0x22447B0);
ShowFlags(0x22447F8);
ShowFlags(0x22447F8);
ShowFlags(0x2244840);
ShowFlags(0x2244840);
ShowFlags(0x2244888);
ShowFlags(0x2244888);
ShowFlags(0x22448D0);
ShowFlags(0x22448D0);
ShowFlags(0x2244918);
ShowFlags(0x2244918);
ShowFlags(0x2244960);
ShowFlags(0x2244960);
ShowFlags(0x22449A8);
ShowFlags(0x22449A8);
ShowFlags(0x22449F0);
ShowFlags(0x22449F0);
ShowFlags(0x2240550);
ShowFlags(0x2240550);
ShowFlags(0x2244A38);
ShowFlags(0x2244A38);
ShowFlags(0x2244A80);
ShowFlags(0x2244A80);
ShowFlags(0x2244AC8);
ShowFlags(0x2244AC8);
ShowFlags(0x2244B10);
ShowFlags(0x2244B10);
ShowFlags(0x2244B58);
ShowFlags(0x2244B58);
ShowFlags(0x2244BA0);
ShowFlags(0x2244BA0);
ShowFlags(0x2244BE8);
ShowFlags(0x2244BE8);
ShowFlags(0x2244C30);
ShowFlags(0x2244C30);
ShowFlags(0x2244C78);
ShowFlags(0x2244C78);
ShowFlags(0x2244CC0);
ShowFlags(0x2244CC0);
ShowFlags(0x2244D08);
ShowFlags(0x2244D08);
ShowFlags(0x2244D50);
ShowFlags(0x2244D50);
ShowFlags(0x2244D98);
ShowFlags(0x2244D98);
ShowFlags(0x2244DE0);
ShowFlags(0x2244DE0);
ShowFlags(0x22406B8);
ShowFlags(0x22406B8);
ShowFlags(0x2244E28);
ShowFlags(0x2244E28);
ShowFlags(0x2244E70);
ShowFlags(0x2244E70);
ShowFlags(0x2244EB8);
ShowFlags(0x2244EB8);
ShowFlags(0x2244F00);
ShowFlags(0x2244F00);
ShowFlags(0x2244F48);
ShowFlags(0x2244F48);
ShowFlags(0x2244F90);
ShowFlags(0x2244F90);
ShowFlags(0x2244FD8);
ShowFlags(0x2244FD8);
ShowFlags(0x2245020);
ShowFlags(0x2245020);
ShowFlags(0x2245068);
ShowFlags(0x2245068);
ShowFlags(0x22450B0);
ShowFlags(0x22450B0);
ShowFlags(0x22450F8);
ShowFlags(0x22450F8);
ShowFlags(0x2245140);
ShowFlags(0x2245140);
ShowFlags(0x2245188);
ShowFlags(0x2245188);
ShowFlags(0x22451D0);
ShowFlags(0x22451D0);
ShowFlags(0x2245218);
ShowFlags(0x2245218);
ShowFlags(0x2245260);
ShowFlags(0x2245260);
ShowFlags(0x22452A8);
ShowFlags(0x22452A8);
ShowFlags(0x22452F0);
ShowFlags(0x22452F0);
ShowFlags(0x2245338);
ShowFlags(0x2245338);
ShowFlags(0x2245380);
ShowFlags(0x2245380);
ShowFlags(0x22453C8);
ShowFlags(0x22453C8);
ShowFlags(0x2245410);
ShowFlags(0x2245410);
ShowFlags(0x2245458);
ShowFlags(0x2245458);
ShowFlags(0x2240700);
ShowFlags(0x2240700);
ShowFlags(0x22454A0);
ShowFlags(0x22454A0);
ShowFlags(0x22454E8);
ShowFlags(0x22454E8);
ShowFlags(0x2240748);
ShowFlags(0x2240748);
ShowFlags(0x2245530);
ShowFlags(0x2245530);
ShowFlags(0x2245578);
ShowFlags(0x2245578);
ShowFlags(0x22455C0);
ShowFlags(0x22455C0);
ShowFlags(0x2245608);
ShowFlags(0x2245608);
ShowFlags(0x2245650);
ShowFlags(0x2245650);
ShowFlags(0x2245698);
ShowFlags(0x2245698);
ShowFlags(0x22456E0);
ShowFlags(0x22456E0);
ShowFlags(0x2245728);
ShowFlags(0x2245728);
ShowFlags(0x2245770);
ShowFlags(0x2245770);
ShowFlags(0x22457B8);
ShowFlags(0x22457B8);
ShowFlags(0x2245800);
ShowFlags(0x2245800);
ShowFlags(0x2245848);
ShowFlags(0x2245848);
ShowFlags(0x2245890);
ShowFlags(0x2245890);
ShowFlags(0x22458D8);
ShowFlags(0x22458D8);
ShowFlags(0x2240868);
ShowFlags(0x2240868);
ShowFlags(0x2245920);
ShowFlags(0x2245920);
ShowFlags(0x2245968);
ShowFlags(0x2245968);
ShowFlags(0x2240820);
ShowFlags(0x2240820);
ShowFlags(0x22459B0);
ShowFlags(0x22459B0);
ShowFlags(0x22459F8);
ShowFlags(0x22459F8);
ShowFlags(0x2245A40);
ShowFlags(0x2245A40);
ShowFlags(0x2245A88);
ShowFlags(0x2245A88);
ShowFlags(0x2245AD0);
ShowFlags(0x2245AD0);
ShowFlags(0x2245B18);
ShowFlags(0x2245B18);
ShowFlags(0x2245B60);
ShowFlags(0x2245B60);
ShowFlags(0x2245BA8);
ShowFlags(0x2245BA8);
ShowFlags(0x2245BF0);
ShowFlags(0x2245BF0);
ShowFlags(0x2245C38);
ShowFlags(0x2245C38);
ShowFlags(0x2245C80);
ShowFlags(0x2245C80);
ShowFlags(0x2245CC8);
ShowFlags(0x2245CC8);
ShowFlags(0x2245D10);
ShowFlags(0x2245D10);
ShowFlags(0x2245D58);
ShowFlags(0x2245D58);
ShowFlags(0x2245DA0);
ShowFlags(0x2245DA0);
ShowFlags(0x2245DE8);
ShowFlags(0x2245DE8);
ShowFlags(0x2245E30);
ShowFlags(0x2245E30);
ShowFlags(0x2245E78);
ShowFlags(0x2245E78);
ShowFlags(0x2245EC0);
ShowFlags(0x2245EC0);
ShowFlags(0x2245F08);
ShowFlags(0x2245F08);
ShowFlags(0x2245F50);
ShowFlags(0x2245F50);
ShowFlags(0x2245F98);
ShowFlags(0x2245F98);
ShowFlags(0x2245FE0);
ShowFlags(0x2245FE0);
ShowFlags(0x2246028);
ShowFlags(0x2246028);
ShowFlags(0x2246070);
ShowFlags(0x2246070);
ShowFlags(0x22460B8);
ShowFlags(0x22460B8);
ShowFlags(0x2246100);
ShowFlags(0x2246100);
ShowFlags(0x2246148);
ShowFlags(0x2246148);
ShowFlags(0x2246190);
ShowFlags(0x2246190);
ShowFlags(0x22461D8);
ShowFlags(0x22461D8);
ShowFlags(0x2246220);
ShowFlags(0x2246220);
ShowFlags(0x2246268);
ShowFlags(0x2246268);
ShowFlags(0x22462B0);
ShowFlags(0x22462B0);
ShowFlags(0x22462F8);
ShowFlags(0x22462F8);
ShowFlags(0x2246340);
ShowFlags(0x2246340);
ShowFlags(0x2246388);
ShowFlags(0x2246388);
ShowFlags(0x22463D0);
ShowFlags(0x22463D0);
ShowFlags(0x2246418);
ShowFlags(0x2246418);
ShowFlags(0x2246460);
ShowFlags(0x2246460);
ShowFlags(0x22464A8);
ShowFlags(0x22464A8);
ShowFlags(0x22464F0);
ShowFlags(0x22464F0);
ShowFlags(0x2246538);
ShowFlags(0x2246538);
ShowFlags(0x2246580);
ShowFlags(0x2246580);
ShowFlags(0x22465C8);
ShowFlags(0x22465C8);
ShowFlags(0x2246610);
ShowFlags(0x2246610);
ShowFlags(0x2246658);
ShowFlags(0x2246658);
ShowFlags(0x22466A0);
ShowFlags(0x22466A0);
ShowFlags(0x22466E8);
ShowFlags(0x22466E8);
ShowFlags(0x2246730);
ShowFlags(0x2246730);
ShowFlags(0x2246778);
ShowFlags(0x2246778);
ShowFlags(0x22467C0);
ShowFlags(0x22467C0);
ShowFlags(0x2246808);
ShowFlags(0x2246808);
ShowFlags(0x2246850);
ShowFlags(0x2246850);
ShowFlags(0x2246898);
ShowFlags(0x2246898);
ShowFlags(0x22468E0);
ShowFlags(0x22468E0);
ShowFlags(0x2246928);
ShowFlags(0x2246928);
ShowFlags(0x2246970);
ShowFlags(0x2246970);
ShowFlags(0x22469B8);
ShowFlags(0x22469B8);
ShowFlags(0x2246A00);
ShowFlags(0x2246A00);
ShowFlags(0x2246A48);
ShowFlags(0x2246A48);
ShowFlags(0x2246A90);
ShowFlags(0x2246A90);
ShowFlags(0x2246AD8);
ShowFlags(0x2246AD8);
ShowFlags(0x2246B20);
ShowFlags(0x2246B20);
ShowFlags(0x2246B68);
ShowFlags(0x2246B68);
ShowFlags(0x2246BB0);
ShowFlags(0x2246BB0);
ShowFlags(0x2246BF8);
ShowFlags(0x2246BF8);
ShowFlags(0x2246C40);
ShowFlags(0x2246C40);
ShowFlags(0x2246C88);
ShowFlags(0x2246C88);
ShowFlags(0x2246CD0);
ShowFlags(0x2246CD0);
ShowFlags(0x2246D18);
ShowFlags(0x2246D18);
ShowFlags(0x2246D60);
ShowFlags(0x2246D60);
ShowFlags(0x2246DA8);
ShowFlags(0x2246DA8);
ShowFlags(0x2246DF0);
ShowFlags(0x2246DF0);
ShowFlags(0x2246E38);
ShowFlags(0x2246E38);
ShowFlags(0x2246E80);
ShowFlags(0x2246E80);
ShowFlags(0x2246EC8);
ShowFlags(0x2246EC8);
ShowFlags(0x2246F10);
ShowFlags(0x2246F10);
ShowFlags(0x2246F58);
ShowFlags(0x2246F58);
ShowFlags(0x2246FA0);
ShowFlags(0x2246FA0);
ShowFlags(0x2246FE8);
ShowFlags(0x2246FE8);
ShowFlags(0x2247030);
ShowFlags(0x2247030);
ShowFlags(0x2247078);
ShowFlags(0x2247078);
ShowFlags(0x22470C0);
ShowFlags(0x22470C0);
ShowFlags(0x2247108);
ShowFlags(0x2247108);
ShowFlags(0x2247150);
ShowFlags(0x2247150);
ShowFlags(0x2247198);
ShowFlags(0x2247198);
ShowFlags(0x22471E0);
ShowFlags(0x22471E0);
ShowFlags(0x2247228);
ShowFlags(0x2247228);
ShowFlags(0x2247270);
ShowFlags(0x2247270);
ShowFlags(0x22472B8);
ShowFlags(0x22472B8);
ShowFlags(0x2247300);
ShowFlags(0x2247300);
ShowFlags(0x2247348);
ShowFlags(0x2247348);
ShowFlags(0x2247390);
ShowFlags(0x2247390);
ShowFlags(0x22473D8);
ShowFlags(0x22473D8);
ShowFlags(0x22405E0);
ShowFlags(0x22405E0);
ShowFlags(0x2247420);
ShowFlags(0x2247420);
ShowFlags(0x2247468);
ShowFlags(0x2247468);
ShowFlags(0x2240628);
ShowFlags(0x2240628);
ShowFlags(0x2240670);
ShowFlags(0x2240670);
ShowFlags(0x22474B0);
ShowFlags(0x22474B0);
ShowFlags(0x22474F8);
ShowFlags(0x22474F8);
ShowFlags(0x2247540);
ShowFlags(0x2247540);
ShowFlags(0x2247588);
ShowFlags(0x2247588);
ShowFlags(0x22475D0);
ShowFlags(0x22475D0);
ShowFlags(0x2247618);
ShowFlags(0x2247618);
ShowFlags(0x2247660);
ShowFlags(0x2247660);
ShowFlags(0x22476A8);
ShowFlags(0x22476A8);
ShowFlags(0x22476F0);
ShowFlags(0x22476F0);
ShowFlags(0x2247738);
ShowFlags(0x2247738);
ShowFlags(0x2247780);
ShowFlags(0x2247780);
ShowFlags(0x2246DA8);
ShowFlags(0x2246DA8);
ShowFlags(0x2246DF0);
ShowFlags(0x2246DF0);
ShowFlags(0x22477C8);
ShowFlags(0x22477C8);
ShowFlags(0x2247810);
ShowFlags(0x2247810);
ShowFlags(0x2246C88);
ShowFlags(0x2246C88);
ShowFlags(0x2247858);
ShowFlags(0x2247858);
ShowFlags(0x22478A0);
ShowFlags(0x22478A0);
ShowFlags(0x22478E8);
ShowFlags(0x22478E8);
ShowFlags(0x2247930);
ShowFlags(0x2247930);
ShowFlags(0x2247978);
ShowFlags(0x2247978);
ShowFlags(0x22479C0);
ShowFlags(0x22479C0);
ShowFlags(0x22447B0);
ShowFlags(0x22447F8);
ShowFlags(0x2247540);
ShowFlags(0x2242B48);
ShowFlags(0x2247A08);
ShowFlags(0x2247A50);
ShowFlags(0x2243EB0);
ShowFlags(0x2241A20);
ShowFlags(0x2241A68);
ShowFlags(0x2241318);
ShowFlags(0x2243E68);
ShowFlags(0x2243D48);
ShowFlags(0x2243F40);
ShowFlags(0x2243C70);
ShowFlags(0x22440A8);
ShowFlags(0x2243F88);
ShowFlags(0x2244258);
ShowFlags(0x22415A0);
ShowFlags(0x2244570);
ShowFlags(0x2244528);
ShowFlags(0x2244AC8);
ShowFlags(0x2244B10);
ShowFlags(0x2244A80);
ShowFlags(0x22450B0);
ShowFlags(0x2242CF8);
ShowFlags(0x22452F0);
ShowFlags(0x2245380);
ShowFlags(0x2245458);
ShowFlags(0x2240700);
ShowFlags(0x2240748);
ShowFlags(0x2245578);
ShowFlags(0x22455C0);
ShowFlags(0x2245530);
ShowFlags(0x22418B8);
ShowFlags(0x2241AF8);
ShowFlags(0x2240868);
ShowFlags(0x2245920);
ShowFlags(0x2247A98);
ShowFlags(0x2245FE0);
ShowFlags(0x2245F50);
ShowFlags(0x2246028);
ShowFlags(0x2246388);
ShowFlags(0x22464F0);
ShowFlags(0x2246808);
ShowFlags(0x2246898);
ShowFlags(0x2246EC8);
ShowFlags(0x2247030);
ShowFlags(0x22470C0);
ShowFlags(0x2246B20);
ShowFlags(0x2240EE0);
ShowFlags(0x2247270);
ShowFlags(0x2240EE0);
ShowFlags(0x2247AE0);
ShowFlags(0x2247AE0);
ShowFlags(0x2242518);
ShowFlags(0x2247B28);
ShowFlags(0x2247B70);
ShowFlags(0x2247BB8);