//Maya ASCII 2018ff07 scene
//Name: jen_bipedTemplateOLD.ma
//Last modified: Mon, Jul 01, 2019 03:19:05 PM
//Codeset: 1252
requires maya "2018ff07";
requires "stereoCamera" "10.0";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2018.0.0";
requires "rpmaya" "2.0";
requires "CustomNode.py" "Unknown";
requires "elastikSolver" "0.991";
requires "Mayatomr" "2013.0 - 3.10.1.11 ";
requires "MayaExporter" "3.0";
requires "cryPoseReaderPlugin.py" "1.0";
requires "shaveNode" "1.1";
requires "ftb_displayNode.py" "Unknown";
requires "sk_rayShooter" "0.1";
requires "vrayformaya" "2.40.01";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201711281015-8e846c9074";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "11A2202F-4F3A-8C31-BEDA-5EAC1AC081A3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 185.09982237131496 231.63803231349769 563.13008853379529 ;
	setAttr ".r" -type "double3" -11.138352729679893 375.00000000018775 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5949EEA3-408C-4D7E-C42A-28AC206B135D";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 691.06029334587242;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 3.5146046650780249e-07 149.63791645914114 3.6312628375631126 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "2D60E3B6-4ED7-6CCC-506F-2FB0D80B94EB";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "EE867EC7-4E69-BF5A-D716-838BE4365CB9";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "294F62F1-43B7-6225-996D-E183EE2FDBB6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -14.313685106448805 3.9712289316648146 1000.624498381474 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "EF98BAEB-4013-ED20-4F98-5EB6115C2249";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 991.37637714567359;
	setAttr ".ow" 40.73684520901174;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -14.313685106448805 3.9712289316648146 9.2481212358005038 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "6F9CA6F3-48A1-0F80-92AE-C594801A169B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.2425109498276 3.9712289316648146 9.2481212358007294 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "DBEFA1D5-4E58-C5E5-BBF2-7BA649397B17";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1014.5561960562765;
	setAttr ".ow" 4.216048642908504;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -14.313685106448805 3.9712289316648146 9.2481212358005038 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Points";
	rename -uid "4BFE3FC6-4FA6-1091-FA7E-FE9A7BD0A40D";
createNode joint -n "C_hip_01_point" -p "Points";
	rename -uid "7E4BD819-4BCB-D476-A618-F2B7A950B7FE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 111.65479999999998 -1.2609 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 111.65479999999998 -1.2608999999999999 1;
createNode joint -n "C_spine_01_point" -p "C_hip_01_point";
	rename -uid "81C9CB62-41FE-21F1-9EF9-B386FF97AFD1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -1.4210854715202004e-14 2.2204460492503131e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 111.65479999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_02_point" -p "C_spine_01_point";
	rename -uid "4113BF7C-45FD-541D-FED8-E5B915652A00";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 2.6016000000000048 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 114.25639999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_03_point" -p "C_spine_02_point";
	rename -uid "12DAE4F1-41A4-C3DD-844C-109BDC113623";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 2.7165999999999997 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 116.97299999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_04_point" -p "C_spine_03_point";
	rename -uid "695D5DF0-4C89-B2D1-8043-D6AAA572936F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 2.8089999999999975 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 119.78199999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_05_point" -p "C_spine_04_point";
	rename -uid "8F9BAAB1-47DC-D153-BB8A-558C8C10D4A2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.7751999999999981 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 122.55719999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_06_point" -p "C_spine_05_point";
	rename -uid "C32F8DEC-4006-8F72-CC80-DAB0A8C0AB1E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 2.6097000000000037 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 125.16689999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_07_point" -p "C_spine_06_point";
	rename -uid "7668F109-45C9-AD02-5B38-7ABB1BF24817";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 2.8426000000000045 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128.00949999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_08_endpoint" -p "C_spine_07_point";
	rename -uid "CBF6D6E4-441C-E504-6A7E-7A8DFD42BFF9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 2.8839999999999861 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 130.89349999999996 -1.2608999999999997 1;
createNode joint -n "C_chest_01_point" -p "C_spine_08_endpoint";
	rename -uid "EE6E6843-41B5-4643-6750-25B0C196D722";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 130.89349999999996 -1.2608999999999997 1;
createNode joint -n "C_chest_01_endpoint" -p "C_chest_01_point";
	rename -uid "9D82A543-40BE-A2EA-F3AB-1DB093646462";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 26.407600000000002 1.1589999999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.341134762145861 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 157.30109999999996 -0.1019000000000001 1;
createNode joint -n "C_neck_01_point" -p "C_chest_01_endpoint";
	rename -uid "8EC9E297-4B5E-B06E-0757-D38E73179D75";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 1.2186000000000092 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 158.48172617196781 0.19994068987560804 1;
createNode joint -n "C_neck_01_endpoint" -p "C_neck_01_point";
	rename -uid "80E962AA-47F1-87E8-AE0C-02AB6A9A3F7E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 9.9473999999999876 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 168.11914680468797 2.6638583646406389 1;
createNode joint -n "C_head_01_point" -p "C_neck_01_endpoint";
	rename -uid "2E747514-4EA2-57AF-89BD-41936F7F5E18";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -10.534087403519667 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99779330908024089 0.066396629091414694 0
		 0 -0.066396629091414694 0.99779330908024089 0 0 168.11914680468797 2.6638583646406389 1;
createNode joint -n "C_head_02_endpoint" -p "C_head_01_point";
	rename -uid "4FE52FCA-4B92-7C50-D1F0-E9B112178E7F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 16.137499999999989 1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99779330908024089 0.066396629091414694 0
		 0 -0.066396629091414694 0.99779330908024089 0 0 184.22103632997036 3.7353339666033518 1;
createNode joint -n "L_clavicle_01_point" -p "C_chest_01_point";
	rename -uid "8BF23B21-473F-049C-432A-C7A2058A8025";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.5308 21.576200000000028 5.7974 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.1390735961927938 22.6113824612261 -4.4241623972122222 ;
	setAttr ".bps" -type "matrix" 0.92038320164279075 -0.071210076365624875 -0.38447872133288169 0
		 0.06950386403779571 0.99741287598133543 -0.018351231851210795 0 0.38479081981978397 -0.0098325912476396101 0.92295143162128268 0
		 3.5308000000000002 152.46969999999999 4.5365000000000002 1;
createNode joint -n "L_upperArm_01_point" -p "L_clavicle_01_point";
	rename -uid "6CE87871-48EF-90CF-AD91-BD9B08E8D7D6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 16.854799999999983 5.6843418860808015e-14 -6.6613381477509392e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 12.517154515515521 -15.098085808284894 -42.102989239739543 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 0.055968188568662702 0.0241740529909449 0.99813985845187725 0
		 19.043674787048896 151.26946840487273 -1.9438119523214548 1;
createNode joint -n "L_lowerArm_01_point" -p "L_upperArm_01_point";
	rename -uid "78EEC4BB-4918-5E72-97AD-17A998A20EE2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 30.424699999999994 2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -15.649261264951837 0 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 40.783160908570018 129.99596769910653 -2.6475739745700535 1;
createNode joint -n "L_lowerArm_02_endpoint" -p "L_lowerArm_01_point";
	rename -uid "271EB970-45CE-1891-DBBA-DF84FC79EFBC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 30.311200000000007 9.9999999960687092e-05 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 62.096379628329117 109.78520147134776 4.838445110404046 1;
createNode joint -n "L_hand_01_point" -p "L_lowerArm_02_endpoint";
	rename -uid "ACE80EA9-4D2F-7414-6831-F5BE0C4659EB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.7763568394002505e-14 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -14.124473977363357 -3.990875640465581 -7.5780869156801147 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 62.096379628329125 109.78520147134779 4.8384451104040433 1;
createNode joint -n "L_fingerThumb_01_point" -p "L_hand_01_point";
	rename -uid "674E66FD-47C0-A5D9-FA5C-43BF27093A89";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 2.2040000000000006 -2.0656000000000034 3.5167000000000073 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 98.54487132213012 -42.877034473271884 -34.624005437801145 ;
	setAttr ".bps" -type "matrix" 0.034215669834380416 -0.39190359663291968 0.9193698161697319 0
		 -0.158105515943812 0.90620183587919234 0.39217455103221893 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.800654227700853 108.48022610612543 9.277035430943446 1;
createNode joint -n "L_fingerThumb_02_point" -p "L_fingerThumb_01_point";
	rename -uid "9E375595-4648-5D01-2A9F-109405DB0855";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 3.1859999999999893 0 -4.2632564145606011e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -16.360174710131172 ;
	setAttr ".bps" -type "matrix" 0.077364582946845173 -0.63128944472241066 0.77167892175925812 0
		 -0.14206613790602968 0.75912043404634244 0.63525851357833674 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.909665351793215 107.23162124725297 12.206147665260197 1;
createNode joint -n "L_fingerThumb_03_point" -p "L_fingerThumb_02_point";
	rename -uid "C9E24642-43E0-90AE-7686-08912938C937";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.9945999999999771 1.4210854715202004e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -0.28982162202627121 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.14134133188584 105.34116187608726 14.517017364360466 1;
createNode joint -n "L_fingerThumb_04_endpoint" -p "L_fingerThumb_03_point";
	rename -uid "988972CA-4601-52E6-DC54-BA8E8AEF5EF2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.0456999999999965 0 2.8421709430404007e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.379156316371741 103.40677310795286 16.857502915879529 1;
createNode joint -n "L_fingerRing_01_point" -p "L_hand_01_point";
	rename -uid "ACEB8118-4207-61DB-E6DE-20940C4074EF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.0013000000000005 1.3537000000000177 -0.91400000000000858 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4114886835528779 1.3868372799917337 -9.9783009568032934 ;
	setAttr ".bps" -type "matrix" 0.44502365829092017 -0.8301252166375015 0.33592568860375582 0
		 0.89417860762666324 0.39139436904737523 -0.2173823027314975 0 0.0489751082102712 0.39711783211100982 0.91645996431663301 0
		 64.952983296691372 107.9232909697694 4.6175239796548322 1;
createNode joint -n "L_fingerRing_02_point" -p "L_fingerRing_01_point";
	rename -uid "C1E81C2C-41CB-1B96-411F-E594997F7676";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 6.6300000000000026 -2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2440262449084497e-17 2.9262079451077954 -3.4229187104741432 ;
	setAttr ".bps" -type "matrix" 0.38783243019260377 -0.87117459908034034 0.30106614556955319 0
		 0.91915385187445187 0.34113294766463303 -0.19693782928121403 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 67.903490151160142 102.41956078346276 6.8447112950977358 1;
createNode joint -n "L_fingerRing_03_point" -p "L_fingerRing_02_point";
	rename -uid "11FC2760-4EC8-09E3-E299-EBAF004CF7A0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 4.3636000000000053 0 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -11.391015201406221 ;
	setAttr ".bps" -type "matrix" 0.1986567576007307 -0.92138933071003293 0.33403172590830632 0
		 0.9776468124963672 0.16235323008449937 -0.13359692622520214 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 69.595835743548605 98.618103302915813 8.1584435279050549 1;
createNode joint -n "L_fingerRing_04_point" -p "L_fingerRing_03_point";
	rename -uid "BFF13D2E-44B8-F4D5-948C-20A005ED35DD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.3362999999999801 2.8421709430404007e-14 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.6348183636358358 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.059957526331232 96.465461409577955 8.9388418491446089 1;
createNode joint -n "L_fingerRing_05_endpoint" -p "L_fingerRing_04_point";
	rename -uid "6B52D8C5-4D53-1387-700E-D3AE83AC12F4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.6081999999999965 -1.4210854715202004e-14 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.415395871415001 94.040282559412447 9.8304013634531451 1;
createNode joint -n "L_fingerPinky_01_point" -p "L_hand_01_point";
	rename -uid "8CEB4B89-4450-398A-8098-558F8789786C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 2.6527999999999921 0.9514000000000209 -2.0000999999999962 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.6985446305270937 12.330079318326504 -11.52988482840385 ;
	setAttr ".bps" -type "matrix" 0.40798064724639849 -0.89887936776129185 0.1598989483563602 0
		 0.89514247352714638 0.35936181178820792 -0.26377839243576828 0 0.17964337883738254 0.25074881942166105 0.95123776522935222 0
		 64.404861384243503 107.52218719186229 3.6167298557496688 1;
createNode joint -n "L_fingerPinky_02_point" -p "L_fingerPinky_01_point";
	rename -uid "D9680118-4226-B206-4B96-1CB119218103";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 6.4719000000000122 1.4210854715202004e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.7045628864259026 1.4311321538117101 -5.1795253117610942 ;
	setAttr ".bps" -type "matrix" 0.32091604996658324 -0.93362417006291643 0.15924445970951659 0
		 0.88339126468981632 0.23443679069863355 -0.4057822872386761 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 67.045271335157452 101.70472981164797 4.6515798596171889 1;
createNode joint -n "L_fingerPinky_03_point" -p "L_fingerPinky_02_point";
	rename -uid "BDD0A47F-4AAB-ED1A-05C0-898765672CCC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.1919999999999789 0 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -5.4728164868637021 ;
	setAttr ".bps" -type "matrix" 0.23520107046132746 -0.95172735344683812 0.19721942387838678 0
		 0.90997126004631224 0.14432513453941986 -0.38874485389507668 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.0696353666508 98.72460146080715 5.159888175009975 1;
createNode joint -n "L_fingerPinky_04_point" -p "L_fingerPinky_03_point";
	rename -uid "37796875-49E8-CB6A-2129-88A42B1DE022";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.9771999999999963 -2.8421709430404007e-14 -2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -6.1478835646679055 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.534674923166889 96.842846137572096 5.549830419902321 1;
createNode joint -n "L_fingerPinky_05_endpoint" -p "L_fingerPinky_04_point";
	rename -uid "802185FC-4732-395A-64CB-D1967018AEFE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.9315999999999747 1.4210854715202004e-14 2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.798135470221197 94.985206573833665 6.0090061502927483 1;
createNode joint -n "L_handEnd_01_endpoint" -p "L_hand_01_point";
	rename -uid "801BC9D8-4108-79BB-5CCD-A7AC90AAB312";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 10.000099999999989 1.4210854715202004e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 68.035505162807809 102.39910493896902 8.0281732978967106 1;
createNode joint -n "L_fingerMiddle_01_point" -p "L_hand_01_point";
	rename -uid "AD55AC13-47AC-80E9-038D-28A9BF948FB4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.0969000000000193 1.3329000000000093 1.0584999999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.7811822362928273 -2.9856130022393392 -10.194298977387604 ;
	setAttr ".bps" -type "matrix" 0.44240884535745983 -0.79968133071715908 0.40593618076233728 0
		 0.89153106858919962 0.44122509101650526 -0.102434236452839 0 -0.097194481786152323 0.40722252928823865 0.90814263436445442 0
		 65.024896941696994 108.64497371087407 6.4544591170109893 1;
createNode joint -n "L_fingerMiddle_02_point" -p "L_fingerMiddle_01_point";
	rename -uid "3210D3D3-42D1-B82C-88F7-899A7F5DC5C4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 7.0528999999999726 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.026464526741199985 -0.62780782886223463 -1.1872468135798082 ;
	setAttr ".bps" -type "matrix" 0.42275103695428745 -0.80414126788699725 0.41789757361722923 0
		 0.90055327418381204 0.42436884534105884 -0.094418660553473172 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 68.145162287118595 103.00490125345905 9.3174864063096514 1;
createNode joint -n "L_fingerMiddle_03_point" -p "L_fingerMiddle_02_point";
	rename -uid "953C4709-4BBA-37E5-1EA4-2483E46E87DC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 4.0896000000000328 1.4210854715202004e-14 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -4.7366699160683909 ;
	setAttr ".bps" -type "matrix" 0.34694282996047571 -0.83643774782613478 0.4242670936456891 0
		 0.9323868894552978 0.35651646473417486 -0.05958773989101776 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 69.87404492784691 99.716285124308371 11.026520323374697 1;
createNode joint -n "L_fingerMiddle_04_point" -p "L_fingerMiddle_03_point";
	rename -uid "2C190052-4D88-B106-91C5-4A9E12EE2B2B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.7797999999999945 -2.8421709430404007e-14 1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -1.3558966089472477 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 70.838476606570978 97.391155472901261 12.205897990290993 1;
createNode joint -n "L_fingerMiddle_05_endpoint" -p "L_fingerMiddle_04_point";
	rename -uid "F60F43D2-43AC-10B1-F214-328E7A455C5F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.541000000000011 2.8421709430404007e-14 -1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 71.663750057467766 95.244926070679952 13.287241637928338 1;
createNode joint -n "L_fingerIndex_01_point" -p "L_hand_01_point";
	rename -uid "D4B4F437-4FB3-1BA9-C31A-1E85FEBF4A43";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 2.9099999999999966 0.5694000000000301 2.8532000000000082 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 23.135397248223082 -9.4103905349096131 -8.7772601649873199 ;
	setAttr ".bps" -type "matrix" 0.46060384413781436 -0.73439291644218296 0.49850891972462535 0
		 0.79079952408287502 0.59458756291652348 0.14526438908172667 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 64.328752580308674 109.10393549685642 8.2274647732668171 1;
createNode joint -n "L_fingerIndex_02_point" -p "L_fingerIndex_01_point";
	rename -uid "6D72F71C-43CA-7E7E-0BA7-56BEE6D569AC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 7.0085000000000264 0 -1.0658141036401503e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.8545262517234296 ;
	setAttr ".bps" -type "matrix" 0.40640166856417559 -0.7727019017824277 0.48761609363317121 0
		 0.81997406807318451 0.5438741551841616 0.17844727795689863 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 67.556894621948544 103.95694274197136 11.721264537156857 1;
createNode joint -n "L_fingerIndex_03_point" -p "L_fingerIndex_02_point";
	rename -uid "BA60CED7-48DB-B77F-4FA1-63B180CE98E5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 4.0149999999999793 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -1.8456032403229279 ;
	setAttr ".bps" -type "matrix" 0.3797825280139645 -0.78981722230580553 0.48161601589281089 0
		 0.83263738802647802 0.51870616060020713 0.19405900910763185 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 69.188597321233672 100.85454460631493 13.679043153094021 1;
createNode joint -n "L_fingerIndex_04_point" -p "L_fingerIndex_03_point";
	rename -uid "38845796-4788-5D95-F1B2-8B9DFA0F15FD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.2283999999999722 0 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -4.9272656096378951 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.034904706660001 99.094515908128727 14.752276282909548 1;
createNode joint -n "L_fingerIndex_05_endpoint" -p "L_fingerIndex_04_point";
	rename -uid "A086640D-4211-B9BD-926C-7AB8D23602A3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.1548999999999836 1.4210854715202004e-14 1.0658141036401503e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.69616369179171 97.302822800904707 15.750357629348152 1;
createNode joint -n "R_clavicle_01_point" -p "C_chest_01_point";
	rename -uid "6265E344-439B-2EB9-9ED9-699570ED41D1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5308 21.576500000000038 5.7974 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 178.86092640380821 -22.611382461226096 4.4241623972122222 ;
	setAttr ".bps" -type "matrix" 0.92038320164279086 0.071210076365624916 0.38447872133288169 0
		 0.069503864037802385 -0.99741287598133521 0.018351231851194885 0 0.38479081981978275 0.0098325912476568099 -0.92295143162128324 0
		 -3.5308000000000002 152.47 4.5365000000000002 1;
createNode joint -n "R_upperArm_01_point" -p "R_clavicle_01_point";
	rename -uid "28CE8812-443A-5F16-8449-748FF9FD2FA8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -16.854900000000008 0.00079999999985602699 4.8849813083506888e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 12.517154515514648 -15.09808580828555 -42.102989239739323 ;
	setAttr ".bps" -type "matrix" 0.71453411608072082 0.69921809272617719 0.023131272362541089 0
		 0.69735827149685803 -0.7144995968972675 0.056407155650294583 0 0.055968188568664257 -0.024174052990946215 -0.99813985845187725 0
		 -19.04371122227786 151.26896335356437 -1.943835719208117 1;
createNode joint -n "R_lowerArm_01_point" -p "R_upperArm_01_point";
	rename -uid "CE28CC6B-47C6-7434-90EA-B19D4B944BA2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -30.424399999999984 -0.00040000000004170033 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -15.649261264951837 0 ;
	setAttr ".bps" -type "matrix" 0.7031443487533322 0.66677788004824612 -0.24697223223394821 0
		 0.69735827149685803 -0.7144995968972675 0.056407155650294583 0 -0.13885051671191934 -0.21189050170314094 -0.96737942364763185 0
		 -40.783261926872733 129.99595821306463 -2.6476133649372624 1;
createNode joint -n "R_lowerArm_02_endpoint" -p "R_lowerArm_01_point";
	rename -uid "AC070658-4264-1A75-F18E-A58E5C9E8B5E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -30.311300000000006 0.00010000000001753051 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.7031443487533322 0.66677788004824612 -0.24697223223394821 0
		 0.69735827149685803 -0.7144995968972675 0.056407155650294583 0 -0.13885051671191934 -0.21189050170314094 -0.96737942364763185 0
		 -62.096411489412453 109.78498240759852 4.8384416986911827 1;
createNode joint -n "R_hand_01_point" -p "R_lowerArm_02_endpoint";
	rename -uid "A19A4931-4848-01D6-F237-A3AA9298CF19";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.0658141036401503e-14 -1.4210854715202004e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -14.12447397736328 -3.9908756404655459 -7.5780869156801494 ;
	setAttr ".bps" -type "matrix" 0.59390661438172476 0.73860226721520694 -0.31896962905297649 0
		 0.80437175917849646 -0.5371645699521177 0.25385093622881794 0 0.016155693415279337 -0.40733391173914346 -0.91313639611919939 0
		 -62.096411489412453 109.78498240759853 4.8384416986911791 1;
createNode joint -n "R_fingerThumb_01_point" -p "R_hand_01_point";
	rename -uid "01108FE3-4FD1-EDDB-8B18-FE9D6D24F44C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.2039999999999509 2.0655999999999608 -3.5167000000000357 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 98.544871322130177 -42.877034473271863 -34.62400543780123 ;
	setAttr ".bps" -type "matrix" 0.034215669834380409 0.39190359663291996 -0.91936981616973179 0
		 -0.15810551594381214 -0.90620183587919212 -0.3921745510322191 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -61.80068608878419 108.48000704237624 9.2770320192305817 1;
createNode joint -n "R_fingerThumb_02_point" -p "R_fingerThumb_01_point";
	rename -uid "FA35C2AC-4385-2D53-5CC6-D5BBAB3DC134";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -3.1856999999999829 -0.00050000000000238742 9.9999999989108801e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -16.360174710131144 ;
	setAttr ".bps" -type "matrix" 0.077364582946845131 0.63128944472241044 -0.77167892175925823 0
		 -0.14206613790602982 -0.75912043404634244 -0.63525851357833663 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -61.90970657834081 107.23198873309612 12.206067625459749 1;
createNode joint -n "R_fingerThumb_03_point" -p "R_fingerThumb_02_point";
	rename -uid "EBE78F1F-4E6C-FC93-F76D-01A50DE2F44F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.995000000000033 0.00040000000001327862 -0.00020000000000663931 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -0.28982162202650347 ;
	setAttr ".bps" -type "matrix" 0.078082209175541678 0.63512124245145352 -0.76845570854616529 0
		 -0.14167298558420133 -0.7559174583190672 -0.63915378537883993 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -62.141272964875334 105.34094144278805 14.516985701559822 1;
createNode joint -n "R_fingerThumb_04_endpoint" -p "R_fingerThumb_03_point";
	rename -uid "B6428382-447D-F578-4663-F8A84500B28C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.0455000000000041 -0.00029999999999574811 0.00010000000000331966 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.078082209175541678 0.63512124245145352 -0.76845570854616529 0
		 -0.14167298558420133 -0.7559174583190672 -0.63915378537883993 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -62.379128513946988 103.40692235173502 16.857512403654486 1;
createNode joint -n "R_fingerRing_01_point" -p "R_hand_01_point";
	rename -uid "3BF5A4CA-4BEF-F16C-48DF-5E9E349C95E7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -3.001399999999947 -1.3537000000000319 0.91409999999996217 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4114886835535398 1.3868372799917263 -9.9783009568033254 ;
	setAttr ".bps" -type "matrix" 0.44502365829092028 0.8301252166375015 -0.33592568860375566 0
		 0.8941786076266629 -0.39139436904737046 0.21738230273150846 0 0.048975108210282114 -0.39711783211101437 -0.91645996431663046 0
		 -64.953072932866775 107.92295731240232 4.6174611512652817 1;
createNode joint -n "R_fingerRing_02_point" -p "R_fingerRing_01_point";
	rename -uid "FB3EC294-4582-CABC-7A18-EEAB87A50FBB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -6.6293999999999826 -0.00029999999999574811 -0.00029999999998153726 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 2.9262079451078398 -3.4229187104741041 ;
	setAttr ".bps" -type "matrix" 0.38783243019260394 0.87117459908034034 -0.30106614556955297 0
		 0.9191538518744512 -0.34113294766462882 0.19693782928122519 0 0.068863652787654162 -0.3531049842962426 -0.933045908511415 0
		 -67.90359571925535 102.41996175488603 6.8446566345934645 1;
createNode joint -n "R_fingerRing_03_point" -p "R_fingerRing_02_point";
	rename -uid "445D76A5-4B21-E39A-3DE3-F395FAC21BE0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.3640000000000256 0.00010000000000331966 0.00019999999999242846 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -11.391015201406228 ;
	setAttr ".bps" -type "matrix" 0.19865675760073087 0.92138933071003215 -0.33403172590830832 0
		 0.97764681249636676 -0.16235323008449509 0.13359692622521308 0 0.068863652787654162 -0.3531049842962426 -0.933045908511415 0
		 -69.595990756500129 98.61805107020777 8.158342378460242 1;
createNode joint -n "R_fingerRing_04_point" -p "R_fingerRing_03_point";
	rename -uid "E538C8F8-474F-04C0-2B5B-CF8134536388";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.3362999999999801 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.6348183636358331 ;
	setAttr ".bps" -type "matrix" 0.136277258294526 0.92982855998983815 -0.34182942807627131 0
		 0.98827440834844482 -0.10361331522721387 0.11215157025720811 0 0.068863652787654162 -0.3531049842962426 -0.933045908511415 0
		 -70.060112539282713 96.46540917686994 8.9387406996998138 1;
createNode joint -n "R_fingerRing_05_endpoint" -p "R_fingerRing_04_point";
	rename -uid "E60212CF-46A1-F71E-7204-15BCE1F29623";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.6081999999999965 2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.136277258294526 0.92982855998983815 -0.34182942807627131 0
		 0.98827440834844482 -0.10361331522721387 0.11215157025720811 0 0.068863652787654162 -0.3531049842962426 -0.933045908511415 0
		 -70.415550884366496 94.040230326704418 9.8303002140083464 1;
createNode joint -n "R_fingerPinky_01_point" -p "R_hand_01_point";
	rename -uid "6F168C59-4445-4A73-81C5-4183D8CAA7E0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.6527999999999707 -0.95140000000003511 2.0000999999999749 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.6985446305271896 12.330079318326487 -11.529884828403883 ;
	setAttr ".bps" -type "matrix" 0.40798064724639843 0.89887936776129185 -0.15989894835636018 0
		 0.89514247352714638 -0.35936181178820731 0.26377839243577023 0 0.17964337883738463 -0.25074881942166177 -0.95123776522935166 0
		 -64.404893245326832 107.52196812811307 3.6167264440368116 1;
createNode joint -n "R_fingerPinky_02_point" -p "R_fingerPinky_01_point";
	rename -uid "41332237-4E49-6C4C-B314-F9A92AF9AAF3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -6.4714999999999776 -0.0001999999999782176 -9.9999999996214228e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.7045628864257747 1.4311321538117241 -5.1795253117611093 ;
	setAttr ".bps" -type "matrix" 0.32091604996658285 0.93362417006291654 -0.15924445970951656 0
		 0.88339126468981677 -0.23443679069863321 0.40578228723867593 0 0.34151539107860418 -0.27089721342467771 -0.89998996517470864 0
		 -67.045336996814427 101.70496724689019 4.651554856423032 1;
createNode joint -n "R_fingerPinky_03_point" -p "R_fingerPinky_02_point";
	rename -uid "2862FAB1-4521-08EC-4B9C-26A23BC9176F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.1923000000000172 -1.4210854715202004e-14 9.9999999996214228e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -5.47281648686364 ;
	setAttr ".bps" -type "matrix" 0.23520107046132796 0.95172735344683812 -0.19721942387838634 0
		 0.90997126004631246 -0.14432513453942053 0.38874485389507668 0 0.34151539107860418 -0.27089721342467771 -0.89998996517470864 0
		 -68.069763151583658 98.724531719076964 5.1598209461572058 1;
createNode joint -n "R_fingerPinky_04_point" -p "R_fingerPinky_03_point";
	rename -uid "19BBC133-4042-EBBE-F812-12B1D2AD17B5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.9771999999999537 -2.8421709430404007e-14 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -6.1478835646678833 ;
	setAttr ".bps" -type "matrix" 0.13639498190840818 0.96171027321309988 -0.23771781444937964 0
		 0.9299266888129587 -0.041569822649722268 0.36538788058478 0 0.34151539107860418 -0.27089721342467771 -0.89998996517470864 0
		 -68.534802708099875 96.842776395841923 5.5497631910495349 1;
createNode joint -n "R_fingerPinky_05_endpoint" -p "R_fingerPinky_04_point";
	rename -uid "2C095C47-44ED-31CC-501B-7D84548A5F33";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.9316000000000031 0 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13639498190840818 0.96171027321309988 -0.23771781444937964 0
		 0.9299266888129587 -0.041569822649722268 0.36538788058478 0 0.34151539107860418 -0.27089721342467771 -0.89998996517470864 0
		 -68.798263255154083 94.985136832103464 6.0089389214399684 1;
createNode joint -n "R_handEnd_01_endpoint" -p "R_hand_01_point";
	rename -uid "E8D8CF54-4D7A-9232-CEFB-98BD370795FB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -9.9999999999999716 0 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.59390661438172476 0.73860226721520694 -0.31896962905297649 0
		 0.80437175917849646 -0.5371645699521177 0.25385093622881794 0 0.016155693415279337 -0.40733391173914346 -0.91313639611919939 0
		 -68.035477633229689 102.39895973544648 8.0281379892209408 1;
createNode joint -n "R_fingerMiddle_01_point" -p "R_hand_01_point";
	rename -uid "A6D59DB3-4ADB-D5D9-76BC-FD8F0FD959F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -3.0966999999999416 -1.3330000000000268 -1.058600000000034 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.7811822362927288 -2.985613002239345 -10.194298977387639 ;
	setAttr ".bps" -type "matrix" 0.44240884535746 0.79968133071715908 -0.40593618076233706 0
		 0.89153106858920028 -0.44122509101650431 0.10243423645284092 0 -0.097194481786150283 -0.40722252928823943 -0.90814263436445442 0
		 -65.024892074202683 108.6449968174265 6.454457839918307 1;
createNode joint -n "R_fingerMiddle_02_point" -p "R_fingerMiddle_01_point";
	rename -uid "496C9CA8-4521-BA1C-C610-468E28D254F6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -7.0527999999999835 -4.2632564145606011e-14 2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.02646452677886646 -0.62780782886217013 -1.1872468135797016 ;
	setAttr ".bps" -type "matrix" 0.42275103695428934 0.8041412678869968 -0.41789757361722785 0
		 0.90055327418387854 -0.42436884534078578 0.094418660554069847 0 -0.10141676937651722 -0.41625461485156096 -0.90357442112092201 0
		 -68.145113178739791 103.00500432814457 9.3174445355988915 1;
createNode joint -n "R_fingerMiddle_03_point" -p "R_fingerMiddle_02_point";
	rename -uid "4D8BD73C-4A90-9FF1-B5E1-ACA46CB92F64";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.0897000000000148 1.4210854715202004e-14 -1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.4787792071889298e-06 1.1848489498583665e-23 -4.7366699160684869 ;
	setAttr ".bps" -type "matrix" 0.34694282996047054 0.83643774782611258 -0.42426709364573711 0
		 0.93238688683784177 -0.35651647547725229 0.059587716570748038 0 -0.10141679344101823 -0.41625460565002559 -0.90357442265885535 0
		 -69.874038094571731 99.716307784867027 11.026520242421316 1;
createNode joint -n "R_fingerMiddle_04_point" -p "R_fingerMiddle_03_point";
	rename -uid "289D6C8C-4CF9-A5D5-8C7C-BDA2B4EABBE8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.7799000000000547 0 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9095099214875593e-06 -2.9621223746459149e-24 -1.3558966089470894 ;
	setAttr ".bps" -type "matrix" 0.32478294020233045 0.84463967054986644 -0.4255583023358171 0
		 0.94033540261180948 -0.33662433000048309 0.049531717581893904 0 -0.10141682477979744 -0.41625459443126761 -0.90357442430961099 0
		 -70.8385044675789 97.391094489685202 12.205940336047099 1;
createNode joint -n "R_fingerMiddle_05_endpoint" -p "R_fingerMiddle_04_point";
	rename -uid "8E66E6F5-414F-437E-4900-3F929CCB4105";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.5409000000000148 0.00010000000000331966 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.8181918208328448e-06 0 0 ;
	setAttr ".bps" -type "matrix" 0.32478294020233045 0.84463967054986644 -0.4255583023358171 0
		 0.94033539585338821 -0.33662435773969634 0.049531657367677222 0 -0.10141688744376608 -0.41625457199861499 -0.90357442761040363 0
		 -71.663651406798706 95.244915888352068 13.287246379623927 1;
createNode joint -n "R_fingerIndex_01_point" -p "R_hand_01_point";
	rename -uid "0008D5C0-4768-957B-C7F0-0DAB3DE225BB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.9097999999999686 -0.56960000000005095 -2.8533000000000328 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 23.135397248223192 -9.4103905349096166 -8.7772601649873412 ;
	setAttr ".bps" -type "matrix" 0.46060384413781458 0.73439291644218285 -0.49850891972462519 0
		 0.79079952408287468 -0.59458756291652393 -0.14526438908172801 0 -0.40308834202413607 -0.32731128044192653 -0.85462688596819836 0
		 -64.328828149990301 109.10401231986582 8.227438111080513 1;
createNode joint -n "R_fingerIndex_02_point" -p "R_fingerIndex_01_point";
	rename -uid "B3E0CAA6-4142-61C0-DAE8-A1B8C6623F22";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -7.0085000000000122 0 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472925031892e-06 -1.1848489498583665e-23 -3.8545262517234558 ;
	setAttr ".bps" -type "matrix" 0.40640166856417548 0.77270190178242781 -0.48761609363317088 0
		 0.81997405606021534 -0.5438741649387977 -0.1784473034267661 0 -0.40308836646126744 -0.32731126423321344 -0.85462688065005477 0
		 -67.556970191630157 103.95701956498078 11.721237874970548 1;
createNode joint -n "R_fingerIndex_03_point" -p "R_fingerIndex_02_point";
	rename -uid "744E3401-4E09-3422-2349-E5B672D1AE67";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.0146999999999764 -0.0001999999999782176 -9.9999999996214228e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.0921955911446032e-06 0 -1.8456032403227247 ;
	setAttr ".bps" -type "matrix" 0.37978252840086046 0.78981722261996423 -0.4816160150725215 0
		 0.83263736130068422 -0.51870618230178589 -0.19405906577158502 0 -0.40308839686560516 -0.32731124529229344 -0.85462687356385236 0
		 -69.18867465638931 100.85499474585428 13.678991358228368 1;
createNode joint -n "R_fingerIndex_04_point" -p "R_fingerIndex_03_point";
	rename -uid "60A6B2BC-4DC6-545D-4BD7-15B913C9C874";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.2287999999999855 0.00030000000000995897 0.00019999999999953388 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.1990154832839402e-06 2.3696978997167331e-23 -4.9272656096380318 ;
	setAttr ".bps" -type "matrix" 0.30686295925979107 0.83145069929701421 -0.46316828353507705 0
		 0.86218026978544748 -0.44895111636143709 -0.2347084947557557 0 -0.40308846005190607 -0.32731121239017297 -0.8546268563628564 0
		 -70.034964782160131 99.094429045975147 14.752187989527551 1;
createNode joint -n "R_fingerIndex_05_endpoint" -p "R_fingerIndex_04_point";
	rename -uid "4D4D1FE0-4C92-07A6-8BD6-B8A50D25A11F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.1549000000000049 -1.4210854715202004e-14 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.1444815029607994e-06 0 0 ;
	setAttr ".bps" -type "matrix" 0.30686295925979107 0.83145069929701421 -0.46316828353507705 0
		 0.8621802124872131 -0.44895116288807269 -0.23470861623926717 0 -0.40308858260911862 -0.32731114857265825 -0.85462682299950044 0
		 -70.696223773069065 97.30273593406001 15.750269323717308 1;
createNode joint -n "L_upperLeg_01_point" -p "C_hip_01_point";
	rename -uid "ECB93773-4548-811E-6146-96B980751275";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 8.6282 -13.904600000000002 1.5523000000000005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 83.464078632328295 -2.0697366443297662 -84.046990766182176 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.10949094408245386 0.047492860074365817 0.99285253759351888 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 8.6281999999999996 97.750199999999978 0.29140000000000055 1;
createNode joint -n "L_lowerLeg_01_point" -p "L_upperLeg_01_point";
	rename -uid "7D1B4B9C-4743-5A1F-D254-07A626C87255";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 44.887900000000009 -8.8817841970012523e-16 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -5.9516763339186403 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 13.280611611853208 53.133493982820909 1.9125652539180953 1;
createNode joint -n "L_lowerLeg_02_endpoint" -p "L_lowerLeg_01_point";
	rename -uid "EC5D095F-4E31-E1EE-82BF-2AAB6768B1A4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 42.189399999999992 -1.1102230246251565e-16 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 17.150787097976934 11.217261827759259 -0.91527773846706939 1;
createNode joint -n "L_foot_01_point" -p "L_lowerLeg_02_endpoint";
	rename -uid "848D9EE9-434C-8DF1-B0B8-588F7F142E04";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 4.4408920985006262e-16 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.1977769946737951 -2.3168929752546785 65.718211009851316 ;
	setAttr ".bps" -type "matrix" 0.10670166423050126 -0.46307425713110978 0.87987327907654533 0
		 0.055748287886651524 0.88631948663135607 0.45970631496123299 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 17.150787097976934 11.217261827759259 -0.91527773846706895 1;
createNode joint -n "L_foot_02_point" -p "L_foot_01_point";
	rename -uid "752893A2-4EBA-C9A9-3728-54B258BD8C8D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 16.5652 1.7763568394002505e-15 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.6766367104750266 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 18.918321506288031 3.5463441435310008 13.659999104091721 1;
createNode joint -n "L_foot_03_endpoint" -p "L_foot_02_point";
	rename -uid "C49544F0-4311-8D71-2F54-8E85A49B7A8C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 9.5399 -1.7763568394002505e-15 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 19.991175272664378 0.14169543621804426 22.506865441149397 1;
createNode joint -n "R_upperLeg_01_point" -p "C_hip_01_point";
	rename -uid "D6A97954-4D7A-9BEF-F719-E181C3638E93";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -8.6282 -13.904600000000002 1.5523000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -96.535921367671733 2.0697366443297627 84.046990766182176 ;
	setAttr ".bps" -type "matrix" 0.10364511620844863 0.9939584167933686 -0.036115863159516919 0
		 0.10949094408245377 -0.047492860074365373 -0.99285253759351866 0 -0.98856938201123246 0.098949956683044932 -0.11375184843488606 0
		 -8.6281999999999996 97.750199999999978 0.29140000000000033 1;
createNode joint -n "R_lowerLeg_01_point" -p "R_upperLeg_01_point";
	rename -uid "0496886B-47DC-89FB-13F6-A989FE8297F4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -44.887900000000023 -8.8817841970012523e-16 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -5.9516763339185976 ;
	setAttr ".bps" -type "matrix" 0.091733358963365486 0.99352520221239515 0.067027333395546645 0
		 0.11964770529926022 0.05582632787059906 -0.99124560414314367 0 -0.9885693791888962 0.098949955458826677 -0.11375187402753628 0
		 -13.280611611853217 53.133493982820895 1.912565253918074 1;
createNode joint -n "R_lowerLeg_02_endpoint" -p "R_lowerLeg_01_point";
	rename -uid "BBD787BC-43EE-AEC5-4211-6A99F0DE1830";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -42.189399999999971 3.3306690738754696e-15 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.091733358963365486 0.99352520221239515 0.067027333395546645 0
		 0.11964770529926022 0.05582632787059906 -0.99124560414314367 0 -0.9885693791888962 0.098949955458826677 -0.11375187402753628 0
		 -17.150786986502222 11.217261816601301 -0.91527772564000243 1;
createNode joint -n "R_foot_01_point" -p "R_lowerLeg_02_endpoint";
	rename -uid "C8761BAF-4525-9F81-FC77-799CE2BB7FF9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -7.1054273576010019e-15 3.3306690738754696e-16 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.1977769946733199 -2.3168929752546843 65.718211009851288 ;
	setAttr ".bps" -type "matrix" 0.10670168634277075 0.46307425487973192 -0.87987327757989675 0
		 0.055748300489973715 -0.88631948780763092 -0.45970631116496385 0 -0.99272699022646127 -1.2479060285119914e-09 -0.12038738669774093 0
		 -17.150786986502219 11.217261816601294 -0.91527772564000287 1;
createNode joint -n "R_foot_02_point" -p "R_foot_01_point";
	rename -uid "0B01B94E-46EC-3D44-9632-E5BE3F62D213";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -16.565200000000004 1.7763568394002505e-15 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.6766367104749706 ;
	setAttr ".bps" -type "matrix" 0.1124596683271008 0.35688515442258456 -0.92735419854148848 0
		 0.042964472249405417 -0.93414826797075845 -0.35428952506609918 0 -0.99272699022646127 -1.2479058619785377e-09 -0.12038738669774099 0
		 -18.918321761107496 3.5463441696675684 13.659999092126512 1;
createNode joint -n "R_foot_03_endpoint" -p "R_foot_02_point";
	rename -uid "0F84BAA7-4488-4D15-F763-2DBF783A7895";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -9.5399 7.460698725481052e-14 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.1124596683270969 0.35688515442267199 -0.92735419854145529 0
		 0.042964472249414506 -0.93414826797072503 -0.35428952506618616 0 -0.99272699022646127 -1.2479044593370443e-09 -0.12038738669774059 0
		 -19.99117575098116 0.14169548499065021 22.506865410792116 1;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "F2F845C3-498F-90BB-95C2-128B639D99C9";
	setAttr -s 39 ".lnk";
	setAttr -s 38 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "23239322-45F2-94F0-32BE-0C8DF00D93F3";
	setAttr -s 5 ".bsdt";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 2 -1 -2 ;
	setAttr ".bsdt[1].bscd" -type "Int32Array" 0 ;
	setAttr ".bsdt[1].bsdn" -type "string" "pasted_";
	setAttr ".bsdt[2].bscd" -type "Int32Array" 1 -3 ;
	setAttr ".bsdt[2].bsdn" -type "string" "RIG_DuendeGino_setup_0007";
	setAttr ".bsdt[3].bscd" -type "Int32Array" 1 -4 ;
	setAttr ".bsdt[3].bspi" 2;
	setAttr ".bsdt[3].bsdn" -type "string" "jen_bipedTemplate";
	setAttr ".bsdt[4].bscd" -type "Int32Array" 0 ;
	setAttr ".bsdt[4].bspi" 3;
	setAttr ".bsdt[4].bsdn" -type "string" "pasted_";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "9D4EE6A9-4953-1B25-FF61-52B7442F1986";
createNode displayLayerManager -n "layerManager";
	rename -uid "465377B9-41E1-15C8-3263-5F9703368978";
	setAttr ".dli[1]"  4;
	setAttr -s 2 ".dli";
createNode displayLayer -n "defaultLayer";
	rename -uid "866A4D5D-4075-1448-4B9F-4B941A171CE8";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "432CADBA-429B-52EE-4353-7598CD4EA3C1";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "C2D89B73-4648-E341-ADB6-8EA6F899A5AC";
	setAttr ".g" yes;
createNode renderLayerManager -n "jen_bipedTemplate_renderLayerManager";
	rename -uid "4EC2B84C-480E-3BC4-DD8C-B59F58AC0642";
createNode renderLayer -n "jen_bipedTemplate_defaultRenderLayer";
	rename -uid "73AE3BC0-495B-492B-A1B3-8D9CA06424A0";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "7806024E-4234-4BCC-2D4E-CDB966EC2A0B";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 606\n            -height 325\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n"
		+ "            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 605\n            -height 325\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n"
		+ "            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n"
		+ "            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 606\n            -height 325\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1218\n            -height 694\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n"
		+ "            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n"
		+ "            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n"
		+ "            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n"
		+ "            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n"
		+ "                -valueLinesToggle 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n"
		+ "                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n"
		+ "                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n"
		+ "                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n"
		+ "                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n"
		+ "                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n"
		+ "                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n"
		+ "                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n"
		+ "            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n"
		+ "            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"DCF_updateViewportList;updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1218\\n    -height 694\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"DCF_updateViewportList;updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1218\\n    -height 694\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 2 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "8BC179F7-44D6-BEAC-C8F2-97B5071D3A48";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "6E4D9B89-4B0A-6194-AC20-1F90BAFA2940";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "FB0CCE86-41D1-01C6-A059-76B8FBBB2E93";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "37115BFD-4E64-B858-4211-F6A6CCEFC7C7";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "4B5EA2C6-450A-E3D6-9A5D-D1850A93A631";
lockNode -l 1 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "8CCB9196-443B-06EE-C37E-BAB7C672847F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "DFBF8C61-439F-8697-F296-F296303A7BC8";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "27D88B98-48AE-09D9-276C-639622445D55";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "54323193-450D-8D04-E847-62B09146BA40";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "D56E07E2-446F-F2FF-BF2F-30803B880E00";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "760779FF-475A-9EA3-48A4-6D834506C31F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode animCurveTL -n "animCurveTL1";
	rename -uid "94135D43-404D-D698-D0B7-FE9E15746AF6";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode animCurveTU -n "animCurveTU1";
	rename -uid "C1BAD784-49FB-4548-5AFB-C28136C21E15";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "37BCAA6C-48C5-3B62-C248-A98FC4B3F28E";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "9D3968D1-4EFC-F58F-BF07-248CF6DCB049";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "1B3CEFC1-4183-FCF9-20CE-0E87C4FAD015";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "4915BA65-446A-8AF5-77B8-AE8C170D1295";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "2B27B0BC-40A5-B48C-8442-6586560D4B01";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "C4DADFC7-4301-428F-FF25-14B2C6597E74";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "B648ED89-4B88-E961-38A1-A7A9A2F69598";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "1EB2C481-416C-3A0C-2839-D9872A4ECEC7";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "F0630D39-43E7-5A4F-4B29-AAB70DD5C319";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "E1421F10-425B-4A9C-CC42-2CA38AB1ECAC";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "3CF01995-4C17-758F-E885-EFA5458A5410";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "8C0985C2-4BBF-E4E0-E16D-F5AF424EE374";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "030660A3-47D9-CCAF-FAD4-738CE8D76B53";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -4280.7104766039447 -3213.09511041831 ;
	setAttr ".tgi[0].vh" -type "double2" 77.05950341883441 -1158.3332873053041 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "9749DCA5-407E-4434-2E86-248E002DF350";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -853.57139465354885 -479.76188569788036 ;
	setAttr ".tgi[0].vh" -type "double2" 854.76187079671979 478.57140955470936 ;
createNode renderLayerManager -n "RIG_DuendeGino_setup_0007:renderLayerManager";
	rename -uid "B8A2F3A6-4BB7-FDDF-A753-6C8ED45CDC5D";
createNode renderLayer -n "RIG_DuendeGino_setup_0007:defaultRenderLayer";
	rename -uid "03F4C3B8-41EE-F70C-33AC-ADA84FBE954D";
	setAttr ".g" yes;
createNode renderLayerManager -n "RIG_DuendeGino_setup_0007:jen_bipedTemplate_renderLayerManager1";
	rename -uid "03009742-4368-527D-4D55-A6B101BF1A45";
createNode renderLayer -n "RIG_DuendeGino_setup_0007:jen_bipedTemplate_defaultRenderLayer";
	rename -uid "FD48CBE9-4AB4-D6B5-1B37-0D895C54CD96";
	setAttr ".g" yes;
createNode renderLayerManager -n "RIG_DuendeGino_setup_0007:jen_bipedTemplate_renderLayerManager";
	rename -uid "D703C0C5-4381-6ABD-8790-2CBC7B1831C4";
createNode renderLayer -n "RIG_DuendeGino_setup_0007:jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer";
	rename -uid "CA5D2236-4B5B-1C26-A1F0-6C83E283771C";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "F313331E-421E-4BBF-51E4-69832E014F2B";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "349FF8A5-4A8E-EE31-5847-318D5E834968";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "665EE530-403F-4626-239A-9EB4AB565F10";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "005C3CA9-4CFC-6DA6-AD18-AE89E30F711D";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "94220293-47D4-49D4-EED7-C79D82DADE9A";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "99099663-410E-1EBA-770E-40AFF7816D8B";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode animCurveTL -n "RIG_DuendeGino_setup_0007:animCurveTL1";
	rename -uid "8D0A001E-49BC-6A87-C0AC-82BB8CB78630";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode animCurveTU -n "RIG_DuendeGino_setup_0007:animCurveTU1";
	rename -uid "E5B034D8-49E6-DAAF-6D5B-A4853A19DB0C";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "3CD1AC7D-48FE-8D1C-4F1F-729892E77507";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "54B1CAC0-4A24-A1FC-E6ED-13B49E0958EF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "5357AB13-431A-64C8-2F7A-C3A6E43014D1";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "405C4045-4C18-70E9-BAEB-AD903C7ED4BF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "209341FC-4C6F-6576-5FEA-D4964CFB96C6";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "12EE0F57-45A0-CED6-6515-E2ADB6A994F4";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "82793692-4F42-A370-A01F-099AC9DDA4B4";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "8BEBE981-4253-ACFE-5439-27A0195E9615";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "2BE2E00D-4DE8-E70A-6D72-9DA2600A2F6D";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "48337BC9-4FE9-1E0C-261C-418D4E6BF27A";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "B2F76CC5-4887-68DA-ADF4-D3988C1C0AC2";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:pasted__hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "41FE2B66-442A-94FD-BBDD-6DAFF0FC7495";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "BE6D17B8-4D50-1855-211B-B3AF8E4063B7";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -4280.7104766039447 -3213.09511041831 ;
	setAttr ".tgi[0].vh" -type "double2" 77.05950341883441 -1158.3332873053041 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:MayaNodeEditorSavedTabsInfo";
	rename -uid "965C26FD-4B7C-6DC4-3991-D2A5D2D6CECA";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -853.57139465354885 -479.76188569788036 ;
	setAttr ".tgi[0].vh" -type "double2" 854.76187079671979 478.57140955470936 ;
createNode renderLayerManager -n "RIG_DuendeGino_setup_0007:tempModel1:renderLayerManager";
	rename -uid "E1223BB9-4863-DAFD-4581-16BC26B83953";
createNode renderLayer -n "RIG_DuendeGino_setup_0007:tempModel1:defaultRenderLayer";
	rename -uid "4B8B4AE0-47CE-7255-9607-439E78619118";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:tempModel1:hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "040EA480-40C1-4A37-B799-B1A6264F316F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -5607.406058843304 -2708.0140767903522 ;
	setAttr ".tgi[0].vh" -type "double2" 3494.0829411981449 2744.9188372286503 ;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:MayaNodeEditorSavedTabsInfo1";
	rename -uid "46F253F8-4447-7BC6-54B7-F3BC9F1A47AF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 34.57469638087462 -273.86348529331519 ;
	setAttr ".tgi[0].vh" -type "double2" 860.16990166990684 418.0537398647208 ;
	setAttr -s 15 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -98.571426391601563;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 191.42857360839844;
	setAttr ".tgi[0].ni[1].y" -182.85714721679688;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 515.71429443359375;
	setAttr ".tgi[0].ni[2].y" 251.42857360839844;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 205.71427917480469;
	setAttr ".tgi[0].ni[3].y" -197.14285278320313;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 512.85711669921875;
	setAttr ".tgi[0].ni[4].y" -197.14285278320313;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -405.71429443359375;
	setAttr ".tgi[0].ni[5].y" 178.57142639160156;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" -98.571426391601563;
	setAttr ".tgi[0].ni[6].y" 230;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -405.71429443359375;
	setAttr ".tgi[0].ni[7].y" -52.857143402099609;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -712.85711669921875;
	setAttr ".tgi[0].ni[8].y" 230;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -405.71429443359375;
	setAttr ".tgi[0].ni[9].y" 280;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 208.57142639160156;
	setAttr ".tgi[0].ni[10].y" 230;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 515.71429443359375;
	setAttr ".tgi[0].ni[11].y" 20;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 208.57142639160156;
	setAttr ".tgi[0].ni[12].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -405.71429443359375;
	setAttr ".tgi[0].ni[13].y" 48.571430206298828;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" -712.85711669921875;
	setAttr ".tgi[0].ni[14].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[14].nvs" 18304;
createNode displayLayer -n "RIG_DuendeGino_setup_0007:mesh_layer";
	rename -uid "485D24BC-49C6-5DBD-8371-0F9468712386";
	setAttr ".v" no;
	setAttr ".do" 1;
createNode renderLayerManager -n "RIG_DuendeGino_setup_0007:tempModel:renderLayerManager";
	rename -uid "ABFCB42C-40EF-1B2B-804E-21AE943CBB12";
createNode renderLayer -n "RIG_DuendeGino_setup_0007:tempModel:defaultRenderLayer";
	rename -uid "44D267A6-4A02-35F0-4E55-C9B376840ED4";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "RIG_DuendeGino_setup_0007:tempModel:hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "BDA75629-41F7-10E9-5AD7-7D9066188D08";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -5607.406058843304 -2708.0140767903522 ;
	setAttr ".tgi[0].vh" -type "double2" 3494.0829411981449 2744.9188372286503 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo7";
	rename -uid "4AA98B06-42B2-934F-B24A-B589DFB313EB";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -742.85711333865333 -322.61903479931897 ;
	setAttr ".tgi[0].vh" -type "double2" 710.71425747303863 336.90474851737002 ;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av -k on ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -av ".ta";
	setAttr -av ".tq";
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -av ".hfe";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 7 ".r";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -k off -cb on ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off -cb on ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "C_hip_01_point.s" "C_spine_01_point.is";
connectAttr "C_spine_01_point.s" "C_spine_02_point.is";
connectAttr "C_spine_02_point.s" "C_spine_03_point.is";
connectAttr "C_spine_03_point.s" "C_spine_04_point.is";
connectAttr "C_spine_04_point.s" "C_spine_05_point.is";
connectAttr "C_spine_05_point.s" "C_spine_06_point.is";
connectAttr "C_spine_06_point.s" "C_spine_07_point.is";
connectAttr "C_spine_07_point.s" "C_spine_08_endpoint.is";
connectAttr "C_spine_08_endpoint.s" "C_chest_01_point.is";
connectAttr "C_chest_01_point.s" "C_chest_01_endpoint.is";
connectAttr "C_chest_01_endpoint.s" "C_neck_01_point.is";
connectAttr "C_neck_01_point.s" "C_neck_01_endpoint.is";
connectAttr "C_neck_01_endpoint.s" "C_head_01_point.is";
connectAttr "C_head_01_point.s" "C_head_02_endpoint.is";
connectAttr "C_chest_01_point.s" "L_clavicle_01_point.is";
connectAttr "L_clavicle_01_point.s" "L_upperArm_01_point.is";
connectAttr "L_upperArm_01_point.s" "L_lowerArm_01_point.is";
connectAttr "L_lowerArm_01_point.s" "L_lowerArm_02_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerThumb_01_point.is";
connectAttr "L_fingerThumb_01_point.s" "L_fingerThumb_02_point.is";
connectAttr "L_fingerThumb_02_point.s" "L_fingerThumb_03_point.is";
connectAttr "L_fingerThumb_03_point.s" "L_fingerThumb_04_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerRing_01_point.is";
connectAttr "L_fingerRing_01_point.s" "L_fingerRing_02_point.is";
connectAttr "L_fingerRing_02_point.s" "L_fingerRing_03_point.is";
connectAttr "L_fingerRing_03_point.s" "L_fingerRing_04_point.is";
connectAttr "L_fingerRing_04_point.s" "L_fingerRing_05_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerPinky_01_point.is";
connectAttr "L_fingerPinky_01_point.s" "L_fingerPinky_02_point.is";
connectAttr "L_fingerPinky_02_point.s" "L_fingerPinky_03_point.is";
connectAttr "L_fingerPinky_03_point.s" "L_fingerPinky_04_point.is";
connectAttr "L_fingerPinky_04_point.s" "L_fingerPinky_05_endpoint.is";
connectAttr "L_hand_01_point.s" "L_handEnd_01_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerMiddle_01_point.is";
connectAttr "L_fingerMiddle_01_point.s" "L_fingerMiddle_02_point.is";
connectAttr "L_fingerMiddle_02_point.s" "L_fingerMiddle_03_point.is";
connectAttr "L_fingerMiddle_03_point.s" "L_fingerMiddle_04_point.is";
connectAttr "L_fingerMiddle_04_point.s" "L_fingerMiddle_05_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerIndex_01_point.is";
connectAttr "L_fingerIndex_01_point.s" "L_fingerIndex_02_point.is";
connectAttr "L_fingerIndex_02_point.s" "L_fingerIndex_03_point.is";
connectAttr "L_fingerIndex_03_point.s" "L_fingerIndex_04_point.is";
connectAttr "L_fingerIndex_04_point.s" "L_fingerIndex_05_endpoint.is";
connectAttr "C_chest_01_point.s" "R_clavicle_01_point.is";
connectAttr "R_clavicle_01_point.s" "R_upperArm_01_point.is";
connectAttr "R_upperArm_01_point.s" "R_lowerArm_01_point.is";
connectAttr "R_lowerArm_01_point.s" "R_lowerArm_02_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerThumb_01_point.is";
connectAttr "R_fingerThumb_01_point.s" "R_fingerThumb_02_point.is";
connectAttr "R_fingerThumb_02_point.s" "R_fingerThumb_03_point.is";
connectAttr "R_fingerThumb_03_point.s" "R_fingerThumb_04_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerRing_01_point.is";
connectAttr "R_fingerRing_01_point.s" "R_fingerRing_02_point.is";
connectAttr "R_fingerRing_02_point.s" "R_fingerRing_03_point.is";
connectAttr "R_fingerRing_03_point.s" "R_fingerRing_04_point.is";
connectAttr "R_fingerRing_04_point.s" "R_fingerRing_05_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerPinky_01_point.is";
connectAttr "R_fingerPinky_01_point.s" "R_fingerPinky_02_point.is";
connectAttr "R_fingerPinky_02_point.s" "R_fingerPinky_03_point.is";
connectAttr "R_fingerPinky_03_point.s" "R_fingerPinky_04_point.is";
connectAttr "R_fingerPinky_04_point.s" "R_fingerPinky_05_endpoint.is";
connectAttr "R_hand_01_point.s" "R_handEnd_01_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerMiddle_01_point.is";
connectAttr "R_fingerMiddle_01_point.s" "R_fingerMiddle_02_point.is";
connectAttr "R_fingerMiddle_02_point.s" "R_fingerMiddle_03_point.is";
connectAttr "R_fingerMiddle_03_point.s" "R_fingerMiddle_04_point.is";
connectAttr "R_fingerMiddle_04_point.s" "R_fingerMiddle_05_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerIndex_01_point.is";
connectAttr "R_fingerIndex_01_point.s" "R_fingerIndex_02_point.is";
connectAttr "R_fingerIndex_02_point.s" "R_fingerIndex_03_point.is";
connectAttr "R_fingerIndex_03_point.s" "R_fingerIndex_04_point.is";
connectAttr "R_fingerIndex_04_point.s" "R_fingerIndex_05_endpoint.is";
connectAttr "C_hip_01_point.s" "L_upperLeg_01_point.is";
connectAttr "L_upperLeg_01_point.s" "L_lowerLeg_01_point.is";
connectAttr "L_lowerLeg_01_point.s" "L_lowerLeg_02_endpoint.is";
connectAttr "L_foot_02_point.s" "L_foot_03_endpoint.is";
connectAttr "C_hip_01_point.s" "R_upperLeg_01_point.is";
connectAttr "R_upperLeg_01_point.s" "R_lowerLeg_01_point.is";
connectAttr "R_lowerLeg_01_point.s" "R_lowerLeg_02_endpoint.is";
connectAttr "R_foot_02_point.s" "R_foot_03_endpoint.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":ikSystem.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":defaultHardwareRenderGlobals.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":defaultHardwareRenderGlobals.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "jen_bipedTemplate_renderLayerManager.rlmi[0]" "jen_bipedTemplate_defaultRenderLayer.rlid"
		;
connectAttr ":TurtleDefaultBakeLayer.idx" ":TurtleBakeLayerManager.bli[0]";
connectAttr ":TurtleRenderOptions.msg" ":TurtleDefaultBakeLayer.rset";
connectAttr "RIG_DuendeGino_setup_0007:renderLayerManager.rlmi[0]" "RIG_DuendeGino_setup_0007:defaultRenderLayer.rlid"
		;
connectAttr "RIG_DuendeGino_setup_0007:jen_bipedTemplate_renderLayerManager1.rlmi[0]" "RIG_DuendeGino_setup_0007:jen_bipedTemplate_defaultRenderLayer.rlid"
		;
connectAttr "RIG_DuendeGino_setup_0007:jen_bipedTemplate_renderLayerManager.rlmi[0]" "RIG_DuendeGino_setup_0007:jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer.rlid"
		;
connectAttr "RIG_DuendeGino_setup_0007:tempModel1:renderLayerManager.rlmi[0]" "RIG_DuendeGino_setup_0007:tempModel1:defaultRenderLayer.rlid"
		;
connectAttr ":initialShadingGroup.msg" "RIG_DuendeGino_setup_0007:MayaNodeEditorSavedTabsInfo1.tgi[0].ni[3].dn"
		;
connectAttr "layerManager.dli[1]" "RIG_DuendeGino_setup_0007:mesh_layer.id";
connectAttr "RIG_DuendeGino_setup_0007:tempModel:renderLayerManager.rlmi[0]" "RIG_DuendeGino_setup_0007:tempModel:defaultRenderLayer.rlid"
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "jen_bipedTemplate_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "RIG_DuendeGino_setup_0007:defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "RIG_DuendeGino_setup_0007:jen_bipedTemplate_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "RIG_DuendeGino_setup_0007:jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "RIG_DuendeGino_setup_0007:tempModel1:defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "RIG_DuendeGino_setup_0007:tempModel:defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
// End of jen_bipedTemplateOLD.ma
