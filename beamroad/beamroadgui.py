# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu May 14 08:00:53 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui
#from guidata.tests.editgroupbox import MainWindow
import PyTango
from PyTango._PyTango import DevFailed
from string import rfind
from hgext.inotify.server import split
from taurus.qt.qtgui.display import TaurusLed

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        os.environ["TANGO_HOST"] = '192.168.130.200:10000'
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(680, 424)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 660, 381))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setMaximumSize(QtCore.QSize(200, 100))
        #self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap("/home/dominik/Dominik Pawlik/workspace/TaurusGui/src/solaris.png"))
        self.label_4.setScaledContents(True)
        #self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1)  # pierwsza wartosc to y a druga to x !!!!!!! ( y w dol a x w prawo)
        self.label_5=QtGui.QLabel(Dialog)
        self.label_5.setText("Pierwszy szereg TaurusLed przy Valve'ach to Status,\ndrugi to interpretacja wartosci valveopen,\nTaurusLed przy innych urzadzeniach to Status: Zielony:ON,Zolty:Fault,Czerwony:OFF")
        self.gridLayout.addWidget(self.label_5,1,0)
#         self.taurusLed_2 = TaurusLed(Dialog)
#         self.taurusLed_2.setObjectName(_fromUtf8("taurusLed_2"))
#         self.gridLayout.addWidget(self.taurusLed_2, 1, 1, 1, 1)
#         self.taurusLed = TaurusLed(Dialog)
#         self.taurusLed.setObjectName(_fromUtf8("taurusLed"))
#         self.gridLayout.addWidget(self.taurusLed, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.pushButton.setText("Wyjdz")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
#         self.taurusLed_3 = TaurusLed(Dialog)
#         self.taurusLed_3.setObjectName(_fromUtf8("taurusLed_3"))
#         self.gridLayout.addWidget(self.taurusLed_3, 2, 1, 1, 1)
#         self.label = QtGui.QLabel(Dialog)
#         self.label.setObjectName(_fromUtf8("label"))
#         self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
#         self.label_2 = QtGui.QLabel(Dialog)
#         self.label_2.setObjectName(_fromUtf8("label_2"))
#         self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
#         self.label_3 = QtGui.QLabel(Dialog)
#         self.label_3.setObjectName(_fromUtf8("label_3"))
#         self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label=[]       #tablica z labelami do zaworow
        self.taurusLed=[]   #tablica z ledami do zaworow
        self.taurusLed_1=[]
        
            ###########
        try:
            self.db = PyTango.Database()
        except Exception as e:
            print 'Connection to Tango db problem: %s' % e
            Dialog.reject()
        self.devList = self.db.get_device_exported_for_class('Valve')   #import urzadzen spod klasy Valve
        self.filterDev=[]
        for i in self.devList:
            self.filterDev.append(i.split("/")[2])
        #print self.filterDev

#         model=self.devList[0];
#         print self.devList
#         print self.devList[0];
#         try:
#             self.deviceProxyModel= PyTango.DeviceProxy(model)
#         except PyTango.DevFailed, e:
#             print 'Prepare Model ---> Received a DevFailed exception:', e
#         print self.deviceProxyModel.state()


        x=0#pierwsza kolumna
        y=0#druga kolumna
        x1=0 #index w pierwszej tablicy
        x2=0 #index w drugiej tablicy
        
################################
#Pierwszy blok ledow i urzadzen
################################

        for i in range(0,len(self.devList)):
            if(self.filterDev[i][0]=="R"):
                
                self.taurusLed.append(TaurusLed())
                self.taurusLed_1.append(TaurusLed(Dialog))
                self.gridLayout_2.addWidget(self.taurusLed[x1],x+3,1,1,1)
                self.gridLayout_2.addWidget(self.taurusLed_1[x1],x+3,2,1,1)
                self.taurusLed[x1].setFixedSize(15,15)
                self.taurusLed_1[x1].setFixedSize(15,15)
                self.label.append(QtGui.QLabel(Dialog))
                self.gridLayout_2.addWidget(self.label[x1],x+3,0,1,1)
                self.label[x1].setText(self.filterDev[i])
                x=x+1
                
                
                try:
                    self.deviceProxyModel= PyTango.DeviceProxy(self.devList[i])
                    #print self.deviceProxyModel.state()
                    #print type(self.deviceProxyModel.state())
                    
                    self.taurusLed[x1].setModel(self.devList[i]+"/state")
                    self.taurusLed_1[x1].setModel(self.devList[i]+"/valveOpen")
#                     if (self.deviceProxyModel.state().__str__()=="OPEN"):
#                         self.taurusLed[x1].setLedColor("Green");
#                         #self.taurusLed[x1].setModel(self.devList[i])
#                     elif(self.deviceProxyModel.state().__str__()=="FAULT"):
#                         self.taurusLed[x1].setLedColor("Black")
#                     else:
#                         self.taurusLed[x1].setLedColor("Red")
#                      
#                     if (self.deviceProxyModel.valveOpen==True):
#                         self.taurusLed_1[x1].setLedColor("Green")
#                     else:
#                         self.taurusLed_1[x1].setLedColor("Red") 
                    x1=x1+1              
                    #if(self.deviceProxyModel.)
                    
                    
                except AttributeError:#, PyTango.DevFailed, e:
                    print 'Prepare Model ---> Received a DevFailed exception:', e
                    self.taurusLed[x1].setLedColor("yellow")
                    self.taurusLed_1[x1].setLedColor("yellow")
                    x1=x1+1
                    
            else:
                self.taurusLed.append(TaurusLed(Dialog))
                self.taurusLed_1.append(TaurusLed(Dialog))
                self.gridLayout_2.addWidget(self.taurusLed[x1],y+3,4,1,1)
                self.gridLayout_2.addWidget(self.taurusLed_1[x1],y+3,5,1,1)
                self.taurusLed[x1].setFixedSize(15,15)
                self.taurusLed_1[x1].setFixedSize(15,15)
                self.label.append(QtGui.QLabel(Dialog))
                self.gridLayout_2.addWidget(self.label[x1],y+3,3,1,1)
                self.label[x1].setText(self.filterDev[i])
                y=y+1
                    
                try:
                    self.deviceProxyModel= PyTango.DeviceProxy(self.devList[i])
                    #print self.deviceProxyModel.state()
                    #print type(self.deviceProxyModel.state())
                    
#                     if (self.deviceProxyModel.state().__str__()=="OPEN"):
#                         self.taurusLed[x1].setLedColor("Green");
#                     elif(self.deviceProxyModel.state().__str__()=="FAULT"):
#                         self.taurusLed[x1].setLedColor("Black")
#                     else:
#                         self.taurusLed[x1].setLedColor("Red")
#                      
#                     if (self.deviceProxyModel.valveOpen==True):
#                         self.taurusLed_1[x1].setLedColor("Green")
#                     else:
#                         self.taurusLed_1[x1].setLedColor("Red")   
                    x1=x1+1            
                    #if(self.deviceProxyModel.)
                    
                    
                except PyTango.DevFailed, e:
                    print 'Prepare Model ---> Received a DevFailed exception:', e
                    self.taurusLed[x1].setLedColor("yellow")
                    self.taurusLed_1[x1].setLedColor("yellow")
                    x1=x1+1  
                
                
        self.filterDev=[]
        for i in self.devList:
            self.filterDev.append(i.split("/")[2])
        #print self.filterDev
################################
#Drugi blok ledow i urzadzen
################################
        self.devList=self.db.get_device_exported_for_class("YagScreen")
        #print self.devList
        self.label_1=[]
        self.taurusLed_2=[]
        self.valveLabel=QtGui.QLabel(Dialog)
        self.gridLayout_2.addWidget(self.valveLabel)
        for i in range(0,len(self.devList)):
            if(self.filterDev[i][0]=="R"):
                try:
                    self.deviceProxyModel=PyTango.DeviceProxy(self.devList[i])
                    #print self.deviceProxyModel.state()
                    self.label_1.append(QtGui.QLabel(Dialog));
                    self.gridLayout_2.addWidget(self.label_1[x2],x+3,0,1,1)
                    self.label_1[x2].setText(self.filterDev[x2])
                    self.taurusLed_2.append(TaurusLed(Dialog))
                    self.gridLayout_2.addWidget(self.taurusLed_2[x2],x+3,1,1,1)
                    self.taurusLed_2[x2].setFixedSize(15,15)
                    x=x+1
                    self.taurusLed_2[x2].setModel(self.devList[i]+"/state")
#                     if(self.deviceProxyModel.state().__str__()=="ON"):
#                         self.taurusLed_2[x2].setLedColor("Green")
#                     else:
#                         self.taurusLed_2[x2].setLedColor("Red")
                    x2=x2+1      
                except PyTango.DevFailed,e:
                    print 'Prepare Model ---> Received a DevFailed exception:', e
                    x2=x2+1
            else:
                try:
                    self.deviceProxyModel=PyTango.DeviceProxy(self.devList[i])
                    #print self.deviceProxyModel.state()
                    self.label_1.append(QtGui.QLabel(Dialog));
                    self.gridLayout_2.addWidget(self.label_1[x2],y+3,3,1,1)
                    self.label_1[x2].setText(self.filterDev[x2])
                    self.taurusLed_2.append(TaurusLed(Dialog))
                    self.gridLayout_2.addWidget(self.taurusLed_2[x2],y+3,4,1,1)
                    self.taurusLed_2[x2].setFixedSize(15,15)
                    y=y+1
                    self.taurusLed_2[x2].setModel(self.devList[i]+"/state")
#                     if(self.deviceProxyModel.state().__str__()=="ON"):
#                         self.taurusLed_2[x2].setLedColor("Green")
#                     else:
#                         self.taurusLed_2[x2].setLedColor("Red")
                    x2=x2+1
                except PyTango.DevFailed,e:
                    print 'Prepare Model ---> Received a DevFailed exception:', e
                    x2=x2+1  
################################
#Trzeci blok ledow i urzadzen
################################
        self.label_scr=[]
        self.taurusLed_scr=[]
        self.filterDev=[]
        x3=0
        self.devList=self.db.get_device_exported_for_class('Scraper')
        for i in self.devList:
            self.filterDev.append(i.split("/")[2])
        #print self.devList
        #print self.filterDev
        for i in range(0,len(self.devList)):
            if(self.filterDev[i][0]=="R"):
                
                try:
                    self.deviceProxyModel=PyTango.DeviceProxy(self.devList[i])
                    self.label_scr.append(QtGui.QLabel(Dialog))
                    self.taurusLed_scr.append(TaurusLed(Dialog))
                    self.taurusLed_scr[x3].setFixedSize(15,15)
                    self.label_scr[x3].setText(self.devList[i].__str__())
                    self.gridLayout_2.addWidget(self.label_scr[x3],x+3,0)
                    self.gridLayout_2.addWidget(self.taurusLed_scr[x3],x+3,1)
                    #print self.deviceProxyModel.state()
                    if(self.deviceProxyModel.state().__str__()=="ON"):
                        self.taurusLed_scr[x3].setLedColor("Green")
                    else:
                        self.taurusLed_scr[x3].setLedColor("Red")                                        
                except PyTango.DevFailed, e:
                    print 'Prepare Model ---> Received a DevFailed exception:', e
                    self.taurusLed_scr[x3].setLedColor("Yellow")
            else:
                
                try:
                    self.deviceProxyModel=PyTango.DeviceProxy(self.devList[i])
                    self.label_scr.append(QtGui.QLabel(Dialog))
                    self.taurusLed_scr.append(TaurusLed(Dialog))
                    self.taurusLed_scr[x3].setFixedSize(15,15)
                    self.label_scr[x3].setText(self.devList[i].__str__())
                    self.gridLayout_2.addWidget(self.label_scr[x3],y+3,0)
                    self.gridLayout_2.addWidget(self.taurusLed_scr[x3],y+3,1)
                    self.taurusLed_scr[x3].setModel(self.devList[i] + "/state")
#                     if(self.deviceProxyModel.state().__str__()=="ON"):
#                         self.taurusLed_scr[x3].setLedColor("Green")
#                     else:
#                         self.taurusLed_scr[x3].setLedColor("Red")         
                except PyTango.DevFailed, e:
                    print 'Prepare Model ---> Received a DevFailed exception:', e 
                    self.taurusLed_scr[x3].setLedColor("Yellow")
        
#         try:
#             self.deviceInfo= PyTango.Database.get_device_attribute_property(self.db,self.devList[0],1)
#         except PyTango.DevFailed, e:
#             print 'Prepare Model ---> Received a DevFailed exception:', e
#         print self.deviceInfo
        
	       ########

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Beam road GUI", None))
#         self.label.setText(_translate("Dialog", "TextLabel", None))
#         self.label_2.setText(_translate("Dialog", "TextLabel", None))
#         self.label_3.setText(_translate("Dialog", "TextLabel", None))

from taurus.qt.qtgui.display import TaurusLed

if __name__ == "__main__":
    import sys
    
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
