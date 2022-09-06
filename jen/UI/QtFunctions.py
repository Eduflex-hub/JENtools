# -*- coding: utf-8 -*-
########################################
# IMPORTS
########################################
import sys
import os
########################################
# WRAPING PySide and PySide2
########################################
jtools = os.getenv("JENTOOLS")
sys.path.append(jtools)
from jen.functions.Qt import QtCore as core
from jen.functions.Qt import QtWidgets as wdg
########################################


def addCustomGroupBox(Layout=None, _Name=None):
    groupBox = QtGroupBox(Parent=Layout, Name=_Name, HeightValue=100, WidthValue=500)
    Layout.addWidget(groupBox)
    boxLyt = QtLayout(Parent=groupBox, F=True, M1=5, M2=5, M3=5, M4=5)
    QtPushButton(Parent=boxLyt, Name="Test BUtton", W=60, H=30)
    print "addingGroupBox"


def QtContainerWidget(self, Central=False, Parent=None, ParentType=None, NameTab=None):
    widget = wdg.QWidget()

    if Central is True:
        self.setCentralWidget(widget)

    if ParentType is "tab":
        Parent.addTab(widget, NameTab)

    if ParentType is "widget":
        Parent.setWidget(widget)

    return widget


def QtGroupBox(Parent=None, Name=None, HeightValue=180, WidthValue=300):
    box = wdg.QGroupBox(Name)
    Parent.addWidget(box)
    box.setFixedHeight(HeightValue)
    box.setFixedWidth(WidthValue)


def QtLayout(Parent=None, ParentType="Widget", V=False, H=False, G=False, F=False, M1=0, M2=0, M3=0, M4=0, Align="Center"):
    ###############################
    # For Alignment:
    # Vertical: Left, Rigth, HCenter, Justify, Top
    # Horizontal: Top, Bottom, VCenter, Baseline
    # Both: Center
    ###############################
    if Align == "Center":
        Alignment = core.Qt.AlignCenter

    elif Align == "Left":
        Alignment = core.Qt.AlignLeft
    elif Align == "Rigth":
        Alignment = core.Qt.AlignRigth
    elif Align == "HCenter":
        Alignment = core.Qt.AlignHCenter
    elif Align == "Justify":
        Alignment = core.Qt.AlignJustify

    elif Align == "Top":
        Alignment = core.Qt.AlignTop
    elif Align == "Bottom":
        Alignment = core.Qt.AlignBottom
    elif Align == "VCenter":
        Alignment = core.Qt.AlignVCenter
    elif Align == "Baseline":
        Alignment = core.Qt.AlignBaseline

    if V is True:
        if ParentType is "Widget":
            layout = wdg.QVBoxLayout(Parent)
        elif ParentType is "Layout":
            layout = wdg.QVBoxLayout()
            Parent.addLayout(layout)

        layout.setContentsMargins(M1, M2, M3, M4)
        layout.setAlignment(Alignment)

    if H is True:
        if ParentType is "Widget":
            layout = wdg.QHBoxLayout(Parent)
        elif ParentType is "Layout":
            layout = wdg.QHBoxLayout()
            Parent.addLayout(layout)

        layout.setContentsMargins(M1, M2, M3, M4)
        layout.setAlignment(Alignment)

    if F is True:
        if ParentType is "Widget":
            layout = wdg.QFormLayout(Parent)
        elif ParentType is "Layout":
            layout = wdg.QFormLayout()
            Parent.addLayout(layout)

        layout.setContentsMargins(M1, M2, M3, M4)

    if G is True:
        if ParentType is "Widget":
            layout = wdg.QGridLayout(Parent)
        elif ParentType is "Layout":
            layout = wdg.QGridLayout()
            Parent.addLayout(layout)

        layout.setContentsMargins(M1, M2, M3, M4)

    return layout


def QtTabWidget(self, Parent=None, Central=False,):

    tabWdg = wdg.QTabWidget()

    if Parent is not None:
        Parent.addWidget(tabWdg)

    if Central is True:
        self.setCentralWidget(tabWdg)

    return tabWdg


def QtScrollArea(Parent=None, H=False, V=False, R=False):

    scroll = wdg.QScrollArea()
    Parent.addWidget(scroll)

    if R is True:
        scroll.setWidgetResizable(True)
    else:
        scroll.setWidgetResizable(False)

    if H is True:
        scroll.setHorizontalScrollBarPolicy(core.Qt.ScrollBarAlwaysOn)
    else:
        scroll.setHorizontalScrollBarPolicy(core.Qt.ScrollBarAlwaysOff)

    if V is True:
        scroll.setVerticalScrollBarPolicy(core.Qt.ScrollBarAlwaysOn)
    else:
        scroll.setVerticalScrollBarPolicy(core.Qt.ScrollBarAlwaysOff)

    return scroll


def QtPushButton(Parent=None, Name=None, W=25, H=25):

    button = wdg.QPushButton(Name)
    Parent.addWidget(button)
    button.setFixedSize(W, H)

    return button
