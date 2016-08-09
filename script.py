#"2016/05/31-21:00:27,Car Mc1, 1/1,59,3104,""0.000"",""0.0"",P,""50.8"",0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,"
import sys
import datetime
import random

f = open('generated_log.csv','w')
f.write('"Failure occurrence time","Car Info","Annexation conditions","Route No.","Car No.","Kilometers","Speed","Notch Mode","Notch Value","LD_OPEN","RD_OPEN","LD_CLOSE","RD_CLOSE","DOOR_CLOSED","DOOR_E_DISLOCK_ON","DOOR_RB","PASSENGER_MODE_ON","TCCB_ON","COS_ON","ZVS_Deadman_ON","HBCOS_ON","DSDR_ON","MAN","ATP","YARD","ROS_ON","PWMNR_F","PBRBPS_ON","DBS_ON","HCR_ON","TCR_ON","RS_ON","TH_N+T","TH_N+B","TH_EB","FORAR","REVAR","DMR_ON","CarCON","UNCPB","HSCB_POS_ON","EBCU_SD_L","PB_IC_ON","EBS_ON","Derailment","PB_RE_L","NO_RB","SLR_OK","SLR_CUTOUT","B_MAJOR_F_L","B_MIN_F_L","Car_B_IC_OPEN","B_IC_OPEN","TOWING_IC_OPEN","FORCE_R_ON","ZVR_ON","B_A_ON","TP","BLANK","Derailment_cutout","MPL_CUTOUT","ZSP","BLANK","BLANK","MCB_HBCB&TLCB","PAN_FFS","PAN_BFS","PAN_CUT_SW","C_PAN_FW","C_PAN_BW","GS_EARTHING","AUX_COM_OK","MCB_IVCB&LBCB"\n')

initialdate = datetime.datetime.now()

for e in range(6):
    kilometers = 0.0
    speed = 0.0
    date = initialdate
    route = random.random()
    pantografo = 1
    disjuntor = 1
    cabine = 1
    femergencia = 1
    fservico = 1
    festacionamento = 0
    portas = 0
    rele = 1
    mpassageiro = 0
    descarilhamento = 0
    speedchange = 0
    r = 0
    for i in range(3000):
        m = '"'
        m += date.strftime('%Y/%m/%d-%H:%M:%S')
        date += datetime.timedelta(0,1)
        m += ('","Car Mc1", 1/1,%d,%d,"%.3f","%.1f",P,"50.8",0,0,0,0,%d,1,0,%d,1,0,1,0,0,1,0,0,0,0,0,0,%d,0,0,1,0,0,1,0,0,0,0,%d,1,0,0,%d,%d,0,%d,0,1,1,0,0,1,0,%d,%d,0,0,0,0,0,0,0,1,%d,1,0,1,1,0,0,1\n' % (route,(3100+e),kilometers,speed,portas,mpassageiro,cabine,disjuntor,descarilhamento,festacionamento,femergencia,rele,fservico,pantografo))

        r = random.randint(0,100)
        if (r%13) == 0:
            pantografo = 0
        else:
            pantografo = 1

        r = random.randint(0,100)
        if (r%13) == 0:
            disjuntor = 0
        else:
            disjuntor = 1

        if speed < 60:
            speedchange = random.uniform(-2, 5.5)
            femergencia = 1
        elif speed > 88:
            speedchange = random.uniform(-7, 0)
            femergencia = 0
        else:
            speedchange = random.uniform(-4, 3)
            femergencia = 1

        if speedchange < 0:
            fservico = 0
        else:
            fservico = 1

        speed += speedchange

        if speed <= 0:
            speed = 0
            rele = 1
            portas = 0
            festacionamento = 0
        else:
            rele = 0
            portas = 1
            festacionamento = 1

        kilometers += speed*(1.000/3600.000)

        f.write(m)


sys.exit(0)
