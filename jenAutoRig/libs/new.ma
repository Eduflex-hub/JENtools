//Maya ASCII 2018ff08 scene
//Name: new.ma
//Last modified: Tue, Oct 30, 2018 11:46:22 AM
//Codeset: 1252
requires maya "2018ff08";
requires "mtoa" "3.1.0.1";
requires "stereoCamera" "10.0";
requires "CustomNode.py" "Unknown";
requires "sk_rayShooter" "0.1";
requires "ftb_displayNode.py" "Unknown";
requires "MayaExporter" "3.0";
requires "shaveNode" "1.1";
requires "Mayatomr" "2013.0 - 3.10.1.11 ";
requires "cryPoseReaderPlugin.py" "1.0";
requires "elastikSolver" "0.991";
requires "rpmaya" "2.0";
requires "vrayformaya" "2.40.01";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201804211841-f3d65dda2a";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "rig";
	rename -uid "B8B01D63-4BC7-3BBC-FCD7-64B48CA23473";
createNode transform -n "Points" -p "rig";
	rename -uid "D63CBC72-49C2-DCAA-55FA-B588D70B55E6";
createNode joint -n "C_hip_01_JNT" -p "Points";
	rename -uid "B772A07A-49E4-ED8B-E808-0E84A779BCD6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 111.65479999999998 -1.2609 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 111.65479999999998 -1.2608999999999999 1;
createNode joint -n "C_spine_01_JNT" -p "C_hip_01_JNT";
	rename -uid "ADCE76FB-4BDB-BE9F-94C7-9789483D2CC5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -1.4210854715202004e-14 2.2204460492503131e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 111.65479999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_02_JNT" -p "C_spine_01_JNT";
	rename -uid "12111862-4430-2DC7-06DF-379B2003BC83";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 2.6016000000000048 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 114.25639999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_03_JNT" -p "C_spine_02_JNT";
	rename -uid "727F1044-401E-0A06-1AF9-E6A53944D0FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 2.7165999999999997 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 116.97299999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_04_JNT" -p "C_spine_03_JNT";
	rename -uid "5288374E-4BF5-87F6-A87E-D3A3DFA45EC4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 2.8089999999999975 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 119.78199999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_05_JNT" -p "C_spine_04_JNT";
	rename -uid "A08BF5E5-4BFD-D88C-1519-659EC2AD40DE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.7751999999999981 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 122.55719999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_06_JNT" -p "C_spine_05_JNT";
	rename -uid "F39ADADA-400E-2E80-D4A3-809EDE596FAA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 2.6097000000000037 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 125.16689999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_07_JNT" -p "C_spine_06_JNT";
	rename -uid "AA552ACE-40C1-0B3D-4155-3EBDDCB087EC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 2.8426000000000045 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128.00949999999997 -1.2608999999999997 1;
createNode joint -n "C_spine_08_endJNT" -p "C_spine_07_JNT";
	rename -uid "6DBD9C9E-42A9-3C16-C005-E7AFD21940D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 2.8839999999999861 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 130.89349999999996 -1.2608999999999997 1;
createNode joint -n "C_chest_01_JNT" -p "C_spine_08_endJNT";
	rename -uid "47D605DE-4564-AB0B-096A-87BE51078D20";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 130.89349999999996 -1.2608999999999997 1;
createNode joint -n "C_chest_01_endJNT" -p "C_chest_01_JNT";
	rename -uid "EAB3319E-4F12-C20A-1603-1291778045CD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 26.407600000000002 1.1589999999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.341134762145861 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 157.30109999999996 -0.1019000000000001 1;
createNode joint -n "C_neck_01_JNT" -p "C_chest_01_endJNT";
	rename -uid "6A9E51D9-4E72-23BF-D26A-E2B86C7F3FA0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 1.2186000000000092 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 158.48172617196781 0.19994068987560804 1;
createNode joint -n "C_neck_01_endJNT" -p "C_neck_01_JNT";
	rename -uid "1EB97558-4D87-CEAE-0573-47AD1040626D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 9.9473999999999876 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 168.11914680468797 2.6638583646406389 1;
createNode joint -n "C_head_01_JNT" -p "C_neck_01_endJNT";
	rename -uid "E8145E77-4196-BBE7-5A9E-1EA7FA3B153B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -10.534087403519667 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99779330908024089 0.066396629091414694 0
		 0 -0.066396629091414694 0.99779330908024089 0 0 168.11914680468797 2.6638583646406389 1;
createNode joint -n "C_head_02_endJNT" -p "C_head_01_JNT";
	rename -uid "1A2E47A5-4C68-7739-A37C-4EA2535BB67F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 16.137499999999989 1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99779330908024089 0.066396629091414694 0
		 0 -0.066396629091414694 0.99779330908024089 0 0 184.22103632997036 3.7353339666033518 1;
createNode joint -n "L_socket_01_JNT" -p "C_head_01_JNT";
	rename -uid "37F6241F-4A9C-D23A-818B-53BF29A4F43E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 3.1411394476890564 5.5210336209579793 7.2999834485445341 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.8070473586261948 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.1411394476890564 173.14330291748041 10.314311027526863 1;
	setAttr ".radi" 0.5;
createNode joint -n "L_eye_01_JNT" -p "L_socket_01_JNT";
	rename -uid "2A11D6E0-4E15-B704-3A6D-F1B86F71C210";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0047355421143919774 5.5371719346187938 -0.00022900411274560324 ;
	setAttr ".bps" -type "matrix" 0.99533380677680339 -3.9782255734175845e-06 -0.096491518131754245 0
		 -3.9782255734175913e-06 0.99999999660831052 -8.2265137058911854e-05 0 0.096491518131754245 8.2265137058911854e-05 0.9953338033851139 0
		 3.1411394476890564 173.14330291748044 10.314311027526863 1;
	setAttr ".radi" 0.25;
createNode joint -n "L_pupil_01_JNT" -p "L_eye_01_JNT";
	rename -uid "F1FBA3F7-4431-2034-27CB-1488A24043E2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 -8.5265128291212022e-14 1.2764897276721374 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99533380677680339 -3.9782255734175845e-06 -0.096491518131754245 0
		 -3.9782255734175913e-06 0.99999999660831052 -8.2265137058911854e-05 0 0.096491518131754245 8.2265137058911854e-05 0.9953338033851139 0
		 3.2643098793917305 173.14340792808275 11.584844403152799 1;
	setAttr ".radi" 0.25;
createNode joint -n "R_socket_01_JNT" -p "C_head_01_JNT";
	rename -uid "E1DC2444-4871-A7B5-30EC-019E72C1186A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -3.141 5.5210336209579793 7.2999834485445341 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.8070473586261948 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.141 173.14330291748041 10.314311027526863 1;
	setAttr ".radi" 0.5;
createNode joint -n "R_eye_01_JNT" -p "R_socket_01_JNT";
	rename -uid "BBCA6A8F-4939-A715-9728-AC8CCE93C3E4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0047355421143919774 -5.537 -0.00022900411274560386 ;
	setAttr ".bps" -type "matrix" 0.99533409632650083 -3.9782267307117623e-06 0.096488531308553907 0
		 1.1971730218799267e-05 0.99999999654456051 -8.2265160990426461e-05 0 -0.096488530647874146 8.3036454339594412e-05 0.99533409293481023 0
		 -3.141 173.14330291748044 10.314311027526863 1;
	setAttr ".radi" 0.25;
createNode joint -n "R_pupil_01_JNT" -p "R_eye_01_JNT";
	rename -uid "A435B177-46B5-2DE9-7769-C68BC8FD3B83";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 4.4408920985006262e-16 -2.8421709430404007e-14 1.2764897276721339 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99533409632650083 -3.9782267307117623e-06 0.096488531308553907 0
		 1.1971730218799267e-05 0.99999999654456051 -8.2265160990426461e-05 0 -0.096488530647874146 8.3036454339594412e-05 0.99533409293481023 0
		 -3.2641666182101887 173.14340891266139 11.584844772760009 1;
	setAttr ".radi" 0.25;
createNode joint -n "C_neck_01_rib2JNT" -p "C_neck_01_JNT";
	rename -uid "8C469247-4D0D-E674-85F5-D79958450A61";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -7.7541922198845499e-16 8.2895000000000039 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90 -3.1805546814635168e-15 90.000000000000043 ;
	setAttr ".bps" -type "matrix" -6.6613381477509392e-16 0.96883815195128109 0.24769464128968724 0
		 -5.5511151231257839e-17 0.24769464128968718 -0.96883815195128109 0 -1.0000000000000002 -4.8403189054421922e-16 -1.2374833222623585e-16 0
		 -7.7541922198845499e-16 166.51291003256796 2.2532054188464632 1;
	setAttr ".radi" 0.8;
createNode joint -n "C_neck_01_rib1JNT" -p "C_neck_01_JNT";
	rename -uid "19165B9F-47AB-8CFE-32DA-CA8E570DB1AA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.3169948137406351e-17 4.9736999999999512 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999986 0 90.000000000000014 ;
	setAttr ".bps" -type "matrix" -2.2204460492503131e-16 0.96883815195128087 0.24769464128968713 0
		 -2.2204460492503131e-16 0.24769464128968713 -0.96883815195128087 0 -1 -2.7012454345353553e-16 1.6012602591910369e-16 0
		 -1.3169948137406351e-17 163.30043648832785 1.4318995272581128 1;
	setAttr ".radi" 0.8;
createNode joint -n "C_neck_01_rib0JNT" -p "C_neck_01_JNT";
	rename -uid "757394DC-48DD-6300-FABA-D0975C369218";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 7.4907932571364209e-16 1.6579000000000121 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90 -3.1805546814635168e-15 90.000000000000043 ;
	setAttr ".bps" -type "matrix" -6.6613381477509392e-16 0.96883815195128109 0.24769464128968724 0
		 -5.5511151231257839e-17 0.24769464128968718 -0.96883815195128109 0 -1.0000000000000002 -4.8403189054421922e-16 -1.2374833222623585e-16 0
		 7.4907932571364209e-16 160.08796294408785 0.61059363566977642 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_clavicle_01_JNT" -p "C_chest_01_JNT";
	rename -uid "F01BCE13-4CEA-7288-0B56-8DB3A7CA87FE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.5308 21.576200000000028 5.7974 ;
	setAttr ".r" -type "double3" 0 0 12.000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.1390735961927938 22.6113824612261 -4.4241623972122222 ;
	setAttr ".bps" -type "matrix" 0.92038320164279075 -0.071210076365624875 -0.38447872133288169 0
		 0.06950386403779571 0.99741287598133543 -0.018351231851210795 0 0.38479081981978397 -0.0098325912476396101 0.92295143162128268 0
		 3.5308000000000002 152.46969999999999 4.5365000000000002 1;
createNode joint -n "L_upperArm_01_JNT" -p "L_clavicle_01_JNT";
	rename -uid "0BA7CC52-4D61-7DE1-6626-4198A40CC316";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 16.854799999999983 5.6843418860808015e-14 -6.6613381477509392e-15 ;
	setAttr ".r" -type "double3" 0 0 29.999999999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 12.517154515515521 -15.098085808284894 -42.102989239739543 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 0.055968188568662702 0.0241740529909449 0.99813985845187725 0
		 19.043674787048896 151.26946840487273 -1.9438119523214548 1;
createNode joint -n "L_lowerArm_01_JNT" -p "L_upperArm_01_JNT";
	rename -uid "E15C7E62-4945-DE37-FEAA-3ABE6EF639AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 30.424699999999994 2.8421709430404007e-14 0 ;
	setAttr ".r" -type "double3" 0 14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -15.649261264951837 0 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 40.783160908570018 129.99596769910653 -2.6475739745700535 1;
createNode joint -n "L_lowerArm_02_endJNT" -p "L_lowerArm_01_JNT";
	rename -uid "72BA832A-405C-681C-F30B-6FBB8CC467E9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 30.311200000000007 9.9999999960687092e-05 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 62.096379628329117 109.78520147134776 4.838445110404046 1;
createNode joint -n "L_hand_01_JNT" -p "L_lowerArm_02_endJNT";
	rename -uid "2EC4BBCF-407E-FC27-DE26-17A4C06BA55B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.7763568394002505e-14 2.8421709430404007e-14 3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 8 0 14.999999999999998 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -14.124473977363357 -3.990875640465581 -7.5780869156801147 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 62.096379628329125 109.78520147134779 4.8384451104040433 1;
createNode joint -n "L_fingerThumb_01_JNT" -p "L_hand_01_JNT";
	rename -uid "B943CEFF-4638-E1FA-6030-17B343040A0C";
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
createNode joint -n "L_fingerThumb_02_JNT" -p "L_fingerThumb_01_JNT";
	rename -uid "8DEE3F39-4EA5-5268-B7C1-7385B66B1980";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 3.1859999999999893 0 -4.2632564145606011e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -16.360174710131172 ;
	setAttr ".bps" -type "matrix" 0.077364582946845173 -0.63128944472241066 0.77167892175925812 0
		 -0.14206613790602968 0.75912043404634244 0.63525851357833674 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.909665351793215 107.23162124725297 12.206147665260197 1;
createNode joint -n "L_fingerThumb_03_JNT" -p "L_fingerThumb_02_JNT";
	rename -uid "E948ACE2-4C05-5DF8-4807-31939C4C680F";
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
createNode joint -n "L_fingerThumb_04_endJNT" -p "L_fingerThumb_03_JNT";
	rename -uid "7BFCF898-4336-6568-A18A-23A00AFA7369";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.0456999999999965 0 2.8421709430404007e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.379156316371741 103.40677310795286 16.857502915879529 1;
createNode joint -n "L_fingerRing_01_JNT" -p "L_hand_01_JNT";
	rename -uid "38AB8C82-4583-E34B-940C-D1BD8EE1E220";
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
createNode joint -n "L_fingerRing_02_JNT" -p "L_fingerRing_01_JNT";
	rename -uid "B7B47025-4A1A-5CD5-7305-2CA033904601";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 6.6300000000000026 -2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2440262449084497e-17 2.9262079451077954 -3.4229187104741428 ;
	setAttr ".bps" -type "matrix" 0.38783243019260377 -0.87117459908034034 0.30106614556955319 0
		 0.91915385187445187 0.34113294766463303 -0.19693782928121403 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 67.903490151160142 102.41956078346276 6.8447112950977358 1;
createNode joint -n "L_fingerRing_03_JNT" -p "L_fingerRing_02_JNT";
	rename -uid "8B68D18C-43B0-9052-6E7D-C985264BA744";
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
createNode joint -n "L_fingerRing_04_JNT" -p "L_fingerRing_03_JNT";
	rename -uid "068055C4-4870-F5C8-989B-E79CCA112E62";
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
createNode joint -n "L_fingerRing_05_endJNT" -p "L_fingerRing_04_JNT";
	rename -uid "866F8685-4E4E-D395-1662-DC824BE11DA0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.6081999999999965 -1.4210854715202004e-14 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.415395871415001 94.040282559412447 9.8304013634531451 1;
createNode joint -n "L_fingerPinky_01_JNT" -p "L_hand_01_JNT";
	rename -uid "E506FDD6-46B1-DE7D-A90F-61A1CD59EF26";
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
createNode joint -n "L_fingerPinky_02_JNT" -p "L_fingerPinky_01_JNT";
	rename -uid "CB2A0A32-4C45-E269-9231-8FA1F9A3682A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 6.4719000000000122 1.4210854715202004e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.7045628864259026 1.4311321538117101 -5.1795253117610942 ;
	setAttr ".bps" -type "matrix" 0.32091604996658324 -0.93362417006291643 0.15924445970951659 0
		 0.88339126468981632 0.23443679069863355 -0.4057822872386761 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 67.045271335157452 101.70472981164797 4.6515798596171889 1;
createNode joint -n "L_fingerPinky_03_JNT" -p "L_fingerPinky_02_JNT";
	rename -uid "7054E0E2-4435-8534-38C5-BF9985ABB26E";
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
createNode joint -n "L_fingerPinky_04_JNT" -p "L_fingerPinky_03_JNT";
	rename -uid "ADB8E31F-41B7-C1AD-4ED4-44B33B29B3AF";
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
createNode joint -n "L_fingerPinky_05_endJNT" -p "L_fingerPinky_04_JNT";
	rename -uid "D51A9622-433B-AF52-7F6B-41B0DB667628";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.9315999999999747 1.4210854715202004e-14 2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.798135470221197 94.985206573833665 6.0090061502927483 1;
createNode joint -n "L_handEnd_01_endJNT" -p "L_hand_01_JNT";
	rename -uid "B798C992-4209-4B4E-953F-B6A76A115CBA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 10.000099999999989 1.4210854715202004e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 68.035505162807809 102.39910493896902 8.0281732978967106 1;
createNode joint -n "L_fingerMiddle_01_JNT" -p "L_hand_01_JNT";
	rename -uid "D58459EE-4A6D-0C3C-F0FF-D986197718BB";
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
createNode joint -n "L_fingerMiddle_02_JNT" -p "L_fingerMiddle_01_JNT";
	rename -uid "69D8BFDA-49BF-36AF-FAD2-D9B5BC31640A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 7.0528999999999726 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.026464526741199985 -0.62780782886223463 -1.1872468135798082 ;
	setAttr ".bps" -type "matrix" 0.42275103695428745 -0.80414126788699725 0.41789757361722923 0
		 0.90055327418381204 0.42436884534105884 -0.094418660553473172 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 68.145162287118595 103.00490125345905 9.3174864063096514 1;
createNode joint -n "L_fingerMiddle_03_JNT" -p "L_fingerMiddle_02_JNT";
	rename -uid "02D9AEAE-4959-B0E8-3B9E-F18BCE89CF6A";
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
createNode joint -n "L_fingerMiddle_04_JNT" -p "L_fingerMiddle_03_JNT";
	rename -uid "DB987E6F-4B3C-EC30-E29E-11AF62ECCBF1";
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
createNode joint -n "L_fingerMiddle_05_endJNT" -p "L_fingerMiddle_04_JNT";
	rename -uid "31AA229A-40DC-653F-8182-A4A5F4D940E2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.541000000000011 2.8421709430404007e-14 -1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 71.663750057467766 95.244926070679952 13.287241637928338 1;
createNode joint -n "L_fingerIndex_01_JNT" -p "L_hand_01_JNT";
	rename -uid "23A49B97-425D-8BE0-D6CD-8F86B0BB9619";
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
createNode joint -n "L_fingerIndex_02_JNT" -p "L_fingerIndex_01_JNT";
	rename -uid "F32B4B9B-4007-0317-D554-908B42643986";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 7.0085000000000264 0 -1.0658141036401503e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.8545262517234296 ;
	setAttr ".bps" -type "matrix" 0.40640166856417559 -0.7727019017824277 0.48761609363317121 0
		 0.81997406807318451 0.5438741551841616 0.17844727795689863 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 67.556894621948544 103.95694274197136 11.721264537156857 1;
createNode joint -n "L_fingerIndex_03_JNT" -p "L_fingerIndex_02_JNT";
	rename -uid "D8978C6B-48B3-E343-FA67-57AEE0C4CC17";
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
createNode joint -n "L_fingerIndex_04_JNT" -p "L_fingerIndex_03_JNT";
	rename -uid "A15BB13E-461F-08E7-320A-BA9F2482E00E";
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
createNode joint -n "L_fingerIndex_05_endJNT" -p "L_fingerIndex_04_JNT";
	rename -uid "F164AC57-4213-459F-20BA-CA9BFCD340DD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.1548999999999836 1.4210854715202004e-14 1.0658141036401503e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.69616369179171 97.302822800904707 15.750357629348152 1;
createNode joint -n "L_lowerArm_01_rib1JNT" -p "L_lowerArm_01_JNT";
	rename -uid "92B76DCB-4791-C676-2F11-11AC86C088D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 11.366699999992704 4.0561197849342534e-05 6.3238303482648917e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999991724204918 2.4265706493099341e-20 0.00016829141981921687 ;
	setAttr ".bps" -type "matrix" 0.70314639705847426 -0.6667757813890185 0.24697206655156428 0
		 0.1388506174379607 -0.21189039850062408 -0.96737943179516883 0 0.69735618613502182 0.71450158598586089 -0.056407741338454234 0
		 48.775620063226114 122.41693255092663 0.15968300962057791 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_lowerArm_01_rib2JNT" -p "L_lowerArm_01_JNT";
	rename -uid "2B6B432C-47FB-FBAF-6171-B9B4FC20D917";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 18.944499999996836 6.5818489602520458e-05 -6.3238303482648917e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999995088809683 2.4265706493099347e-20 0.00022143110414791993 ;
	setAttr ".bps" -type "matrix" 0.70314704382987092 -0.66677511871536499 0.24697201423526619 0
		 0.13885057648675703 -0.21189044045855504 -0.96737942848273095 0 0.69735554214662165 0.7145021919521245 -0.056408027203587938 0
		 54.103924922593507 117.36424117781878 2.0311877663508016 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_lowerArm_01_rib3JNT" -p "L_lowerArm_01_JNT";
	rename -uid "8669E98E-461D-F9AE-7DEE-2E8CC2FF42D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 26.522299999990594 9.4040885386448281e-05 -3.694822225952521e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.99999899627835 1.2132853246549673e-20 0.00016236075583146679 ;
	setAttr ".bps" -type "matrix" 0.70314632487539919 -0.66677585534679473 0.2469720723903209 0
		 0.13885052892838065 -0.21189048918632591 -0.96737942463579862 0 0.69735627654057031 0.71450149007467456 -0.056407838555839702 0
		 59.432231849693217 112.31155192328382 3.9026923558268569 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_lowerArm_01_rib0JNT" -p "L_lowerArm_01_JNT";
	rename -uid "46F6C20F-4ACC-426C-5344-93BD0D64DB93";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 3.7888999999959907 1.4152343695172931e-05 3.6237679523765109e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999987816736024 0 0.00022736176647921805 ;
	setAttr ".bps" -type "matrix" 0.70314711601285074 -0.66677504475753824 0.24697200839648481 0
		 0.1388506649962413 -0.21189034977275706 -0.96737943564212714 0 0.69735545174101277 0.71450228786321024 -0.056407929986185594 0
		 43.44731440081258 127.46962310123834 -1.7118216821529395 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperArm_01_rib0JNT" -p "L_upperArm_01_JNT";
	rename -uid "D19B9306-4DEB-EA8D-6222-F2B3C26C021F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 3.8030874999999895 -2.8421709430404007e-14 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000426 0 0 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 -0.055968188568667809 -0.024174052990950136 -0.9981398584518768 0 0.69735827149685781 0.71449959689726716 -0.056407155650300009 0
		 21.761110552239018 148.61028081665185 -2.0317822051025303 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperArm_01_rib1JNT" -p "L_upperArm_01_JNT";
	rename -uid "DA6313ED-4F87-8183-AF42-36AF2A896E08";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 11.409262499999997 -1.4210854715202004e-14 -2.6645352591003757e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000426 0 0 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 -0.055968188568667809 -0.024174052990950136 -0.9981398584518768 0 0.69735827149685781 0.71449959689726716 -0.056407155650300009 0
		 27.195982082619302 143.29190564021033 -2.2077227106646804 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperArm_01_rib2JNT" -p "L_upperArm_01_JNT";
	rename -uid "6F5BBE30-439E-3BAD-0FC9-D69D07EDF161";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 19.015437499999976 0 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999616 0 0 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 -0.055968188568657977 -0.024174052990940061 -0.99813985845187758 0 0.69735827149685858 0.7144995968972675 -0.056407155650285937 0
		 32.630853612999573 137.97353046376884 -2.3836632162268283 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperArm_01_rib3JNT" -p "L_upperArm_01_JNT";
	rename -uid "B90EE56B-4F86-D562-BE29-61B082CA65B6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 26.621612499999983 1.4210854715202004e-14 1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999631 0 0 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 -0.055968188568658213 -0.0241740529909403 -0.99813985845187758 0 0.69735827149685858 0.7144995968972675 -0.05640715565028627 0
		 38.065725143379865 132.65515528732729 -2.5596037217889762 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_clavicle_01_JNT" -p "C_chest_01_JNT";
	rename -uid "AE8A3369-4F5D-0A3D-9ED5-F5A9D028EB1F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5308 21.576500000000038 5.7974 ;
	setAttr ".r" -type "double3" 0 0 12.000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 178.86092640380821 -22.611382461226096 4.4241623972122222 ;
	setAttr ".bps" -type "matrix" 0.92038320164279086 0.071210076365624916 0.38447872133288169 0
		 0.069503864037802385 -0.99741287598133521 0.018351231851194885 0 0.38479081981978275 0.0098325912476568099 -0.92295143162128324 0
		 -3.5308000000000002 152.47 4.5365000000000002 1;
createNode joint -n "R_upperArm_01_JNT" -p "R_clavicle_01_JNT";
	rename -uid "9838E977-4712-FA2B-4850-42A97EE538D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -16.854900000000008 0.00079999999985602699 4.8849813083506888e-15 ;
	setAttr ".r" -type "double3" 0 0 29.999999999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 12.517154515514648 -15.09808580828555 -42.102989239739323 ;
	setAttr ".bps" -type "matrix" 0.71453411608072082 0.69921809272617719 0.023131272362541089 0
		 0.69735827149685803 -0.7144995968972675 0.056407155650294583 0 0.055968188568664257 -0.024174052990946215 -0.99813985845187725 0
		 -19.04371122227786 151.26896335356437 -1.943835719208117 1;
createNode joint -n "R_lowerArm_01_JNT" -p "R_upperArm_01_JNT";
	rename -uid "B84B8347-4DB2-CA2C-7998-C5ACEEAD1E74";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -30.424399999999984 -0.00040000000004170033 0 ;
	setAttr ".r" -type "double3" 0 14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -15.649261264951837 0 ;
	setAttr ".bps" -type "matrix" 0.7031443487533322 0.66677788004824612 -0.24697223223394821 0
		 0.69735827149685803 -0.7144995968972675 0.056407155650294583 0 -0.13885051671191934 -0.21189050170314094 -0.96737942364763185 0
		 -40.783261926872733 129.99595821306463 -2.6476133649372624 1;
createNode joint -n "R_lowerArm_02_endJNT" -p "R_lowerArm_01_JNT";
	rename -uid "AA175FFE-4B43-E6DC-25F5-CC853DB6D209";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -30.311300000000006 0.00010000000001753051 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.7031443487533322 0.66677788004824612 -0.24697223223394821 0
		 0.69735827149685803 -0.7144995968972675 0.056407155650294583 0 -0.13885051671191934 -0.21189050170314094 -0.96737942364763185 0
		 -62.096411489412453 109.78498240759852 4.8384416986911827 1;
createNode joint -n "R_hand_01_JNT" -p "R_lowerArm_02_endJNT";
	rename -uid "887A6EBA-48D7-D46F-79A3-9ABE21E6E054";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.0658141036401503e-14 -1.4210854715202004e-14 0 ;
	setAttr ".r" -type "double3" 8 0 14.999999999999998 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -14.124473977363278 -3.9908756404655459 -7.5780869156801494 ;
	setAttr ".bps" -type "matrix" 0.59390661438172476 0.73860226721520694 -0.31896962905297649 0
		 0.80437175917849646 -0.5371645699521177 0.25385093622881794 0 0.016155693415279337 -0.40733391173914346 -0.91313639611919939 0
		 -62.096411489412453 109.78498240759853 4.8384416986911791 1;
createNode joint -n "R_fingerThumb_01_JNT" -p "R_hand_01_JNT";
	rename -uid "4284784B-46EC-FE87-EC24-9D94EC2F6699";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.2039999999999509 2.0655999999999608 -3.5167000000000357 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 98.544871322130177 -42.877034473271863 -34.624005437801223 ;
	setAttr ".bps" -type "matrix" 0.034215669834380409 0.39190359663291996 -0.91936981616973179 0
		 -0.15810551594381214 -0.90620183587919212 -0.3921745510322191 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -61.80068608878419 108.48000704237624 9.2770320192305817 1;
createNode joint -n "R_fingerThumb_02_JNT" -p "R_fingerThumb_01_JNT";
	rename -uid "9A40881C-4DC7-4CE7-938D-89B6CA4904F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -3.1856999999999829 -0.00050000000000238742 9.9999999989108801e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -16.360174710131144 ;
	setAttr ".bps" -type "matrix" 0.077364582946845131 0.63128944472241044 -0.77167892175925823 0
		 -0.14206613790602982 -0.75912043404634244 -0.63525851357833663 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -61.90970657834081 107.23198873309612 12.206067625459749 1;
createNode joint -n "R_fingerThumb_03_JNT" -p "R_fingerThumb_02_JNT";
	rename -uid "693E6DEA-4B06-E383-9539-408BBE65F09A";
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
createNode joint -n "R_fingerThumb_04_endJNT" -p "R_fingerThumb_03_JNT";
	rename -uid "005C5AB2-4F05-5017-537F-7092DE3AE3B3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.0455000000000041 -0.00029999999999574811 0.00010000000000331966 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.078082209175541678 0.63512124245145352 -0.76845570854616529 0
		 -0.14167298558420133 -0.7559174583190672 -0.63915378537883993 0 -0.98682923232235364 0.15877595408424783 0.030955817526131718 0
		 -62.379128513946988 103.40692235173502 16.857512403654486 1;
createNode joint -n "R_fingerRing_01_JNT" -p "R_hand_01_JNT";
	rename -uid "6C715D25-43CD-35ED-AC2A-8C80D80FF6FD";
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
createNode joint -n "R_fingerRing_02_JNT" -p "R_fingerRing_01_JNT";
	rename -uid "76AB17CD-4665-ECE3-1944-87A3ED58BDFE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -6.6293999999999826 -0.00029999999999574811 -0.00029999999998153726 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 2.9262079451078398 -3.4229187104741041 ;
	setAttr ".bps" -type "matrix" 0.38783243019260394 0.87117459908034034 -0.30106614556955297 0
		 0.9191538518744512 -0.34113294766462882 0.19693782928122519 0 0.068863652787654162 -0.3531049842962426 -0.933045908511415 0
		 -67.90359571925535 102.41996175488603 6.8446566345934645 1;
createNode joint -n "R_fingerRing_03_JNT" -p "R_fingerRing_02_JNT";
	rename -uid "6ADC2831-4E3B-9246-D79D-EFA18E89CC6B";
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
createNode joint -n "R_fingerRing_04_JNT" -p "R_fingerRing_03_JNT";
	rename -uid "D598330D-4EE0-0E73-995C-269565BF53DA";
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
createNode joint -n "R_fingerRing_05_endJNT" -p "R_fingerRing_04_JNT";
	rename -uid "76228EEC-4BB6-7314-624E-12AC1EE78F54";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.6081999999999965 2.8421709430404007e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.136277258294526 0.92982855998983815 -0.34182942807627131 0
		 0.98827440834844482 -0.10361331522721387 0.11215157025720811 0 0.068863652787654162 -0.3531049842962426 -0.933045908511415 0
		 -70.415550884366496 94.040230326704418 9.8303002140083464 1;
createNode joint -n "R_fingerPinky_01_JNT" -p "R_hand_01_JNT";
	rename -uid "3C519AE7-46C7-B791-4050-A08F8C8FF7A1";
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
createNode joint -n "R_fingerPinky_02_JNT" -p "R_fingerPinky_01_JNT";
	rename -uid "EDFB3D95-4142-1BCA-2423-85AD72D3A332";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -6.4714999999999776 -0.0001999999999782176 -9.9999999996214228e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.7045628864257747 1.4311321538117241 -5.1795253117611093 ;
	setAttr ".bps" -type "matrix" 0.32091604996658285 0.93362417006291654 -0.15924445970951656 0
		 0.88339126468981677 -0.23443679069863321 0.40578228723867593 0 0.34151539107860418 -0.27089721342467771 -0.89998996517470864 0
		 -67.045336996814427 101.70496724689019 4.651554856423032 1;
createNode joint -n "R_fingerPinky_03_JNT" -p "R_fingerPinky_02_JNT";
	rename -uid "E0E0584B-4BA9-1419-7BBE-63BB7CCA520E";
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
createNode joint -n "R_fingerPinky_04_JNT" -p "R_fingerPinky_03_JNT";
	rename -uid "E1661AF8-47FD-FECD-B9A5-5B93219B1F64";
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
createNode joint -n "R_fingerPinky_05_endJNT" -p "R_fingerPinky_04_JNT";
	rename -uid "5B0956E3-4262-CB63-359D-4D8B300D4E1F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.9316000000000031 0 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13639498190840818 0.96171027321309988 -0.23771781444937964 0
		 0.9299266888129587 -0.041569822649722268 0.36538788058478 0 0.34151539107860418 -0.27089721342467771 -0.89998996517470864 0
		 -68.798263255154083 94.985136832103464 6.0089389214399684 1;
createNode joint -n "R_handEnd_01_endJNT" -p "R_hand_01_JNT";
	rename -uid "963C283F-47B7-B833-CF19-BAA9D64BCBD3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -9.9999999999999716 0 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.59390661438172476 0.73860226721520694 -0.31896962905297649 0
		 0.80437175917849646 -0.5371645699521177 0.25385093622881794 0 0.016155693415279337 -0.40733391173914346 -0.91313639611919939 0
		 -68.035477633229689 102.39895973544648 8.0281379892209408 1;
createNode joint -n "R_fingerMiddle_01_JNT" -p "R_hand_01_JNT";
	rename -uid "56FBB5D2-403B-E306-FA52-A9937F0BEDC2";
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
createNode joint -n "R_fingerMiddle_02_JNT" -p "R_fingerMiddle_01_JNT";
	rename -uid "036B1C26-4D5B-B67E-4321-3997D6886D5A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -7.0527999999999835 -4.2632564145606011e-14 2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.02646452677886646 -0.62780782886217013 -1.1872468135797016 ;
	setAttr ".bps" -type "matrix" 0.42275103695428934 0.8041412678869968 -0.41789757361722785 0
		 0.90055327418387854 -0.42436884534078578 0.094418660554069847 0 -0.10141676937651722 -0.41625461485156096 -0.90357442112092201 0
		 -68.145113178739791 103.00500432814457 9.3174445355988915 1;
createNode joint -n "R_fingerMiddle_03_JNT" -p "R_fingerMiddle_02_JNT";
	rename -uid "6869A750-4915-220F-E584-6BA36A771C07";
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
createNode joint -n "R_fingerMiddle_04_JNT" -p "R_fingerMiddle_03_JNT";
	rename -uid "728B7B9D-4274-B9AB-7B3D-BCA8211E0C49";
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
createNode joint -n "R_fingerMiddle_05_endJNT" -p "R_fingerMiddle_04_JNT";
	rename -uid "14A9E1CF-41BC-2360-3E29-C8B643C19B85";
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
createNode joint -n "R_fingerIndex_01_JNT" -p "R_hand_01_JNT";
	rename -uid "5C7F0A5D-4BC7-1F14-2A07-8DADF218997E";
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
createNode joint -n "R_fingerIndex_02_JNT" -p "R_fingerIndex_01_JNT";
	rename -uid "61291949-4978-C748-2B12-1793B787017E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -7.0085000000000122 0 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472925031892e-06 -1.1848489498583665e-23 -3.8545262517234558 ;
	setAttr ".bps" -type "matrix" 0.40640166856417548 0.77270190178242781 -0.48761609363317088 0
		 0.81997405606021534 -0.5438741649387977 -0.1784473034267661 0 -0.40308836646126744 -0.32731126423321344 -0.85462688065005477 0
		 -67.556970191630157 103.95701956498078 11.721237874970548 1;
createNode joint -n "R_fingerIndex_03_JNT" -p "R_fingerIndex_02_JNT";
	rename -uid "4AE13995-430A-A421-470A-1284BC8E3141";
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
createNode joint -n "R_fingerIndex_04_JNT" -p "R_fingerIndex_03_JNT";
	rename -uid "D2153EF2-44D1-3A99-49DA-4C99FB9B1C22";
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
createNode joint -n "R_fingerIndex_05_endJNT" -p "R_fingerIndex_04_JNT";
	rename -uid "6AC6A72F-4030-DDB5-36DF-3FACD6570068";
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
createNode joint -n "R_lowerArm_01_rib1JNT" -p "R_lowerArm_01_JNT";
	rename -uid "3A78419B-4A3C-686E-AC4C-18A9174D6E43";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -11.366737499995367 4.0561197891975098e-05 -3.0611840955430125e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000054584 -2.0733529896093221e-05 179.99983170913563 ;
	setAttr ".bps" -type "matrix" -0.70314235069444631 -0.66678005537122065 0.24697204784963098 0
		 -0.13885026226629296 -0.21189026041722908 -0.96737951301901171 0 0.69736033679043574 -0.71449763841420122 0.056406430236801211 0
		 -48.775690453023209 122.41684074742911 0.15966041792222985 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_lowerArm_01_rib0JNT" -p "R_lowerArm_01_JNT";
	rename -uid "510A081A-430F-B822-0360-ECA9CFCE0865";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.7889124999972594 1.4152343737805495e-05 -1.6523362909026673e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999905 3.8336355865302592e-05 179.99977263898401 ;
	setAttr ".bps" -type "matrix" -0.70314148858744308 -0.66678057354393772 0.24697310333607658 0
		 -0.13885098718200617 -0.21189094784197363 -0.96737925839931704 0 0.69736106170736056 -0.71449695098513011 0.056406175613449551 0
		 -43.44740424048495 127.46958540689862 -1.7118547903442451 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_lowerArm_01_rib2JNT" -p "R_lowerArm_01_JNT";
	rename -uid "F8A6DAD1-4D25-B57C-9E68-A9B07A95FFBD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -18.944562500004608 6.5818489559887894e-05 -3.318474604441235e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000345096 3.2405739314356323e-05 179.99977856962713 ;
	setAttr ".bps" -type "matrix" -0.70314157514305264 -0.66678052151946232 0.24697299736526096 0
		 -0.13885091439536812 -0.21189087882977159 -0.96737928396276784 0 0.69736098892676635 -0.71449702000146997 0.056406201184813376 0
		 -54.103977628515246 117.36409666673904 2.0311744472422575 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_lowerArm_01_rib3JNT" -p "R_lowerArm_01_JNT";
	rename -uid "3353038D-4E0D-DAE3-28C7-2F93DAE2D2C9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -26.522387500002715 9.4040885400659135e-05 -6.5408558889146207e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000471047 -2.6664146459761048e-05 179.99983763977883 ;
	setAttr ".bps" -type "matrix" -0.70314243724990688 -0.6667800033466017 0.24697194187876226 0
		 -0.13885018947977884 -0.21189019140486198 -0.96737953858237069 0 0.69736026400970852 -0.71449770743055341 0.056406455807760561 0
		 -59.432262324555147 112.31135109576523 3.902691512180434 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperArm_01_rib0JNT" -p "R_upperArm_01_JNT";
	rename -uid "B9CA3CED-4B3C-AFD6-80E9-C29B394D97D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.8030499999999847 -4.9999998338989826e-05 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000639 4.8531412986198705e-20 -179.99924671279689 ;
	setAttr ".bps" -type "matrix" -0.71454328442659321 -0.6992086988952535 -0.023132013964703265 0
		 0.055968188568672077 -0.024174052990954226 -0.99813985845187658 0 0.69734887721225913 -0.71450878969484832 0.056406851530684116 0
		 -21.761155060351022 148.60983771100049 -2.0318079249241565 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperArm_01_rib1JNT" -p "R_upperArm_01_JNT";
	rename -uid "CBC0440A-4817-6929-DE88-BB985B2F06D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -11.409149999999997 -0.00014999999832809863 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999844 4.8531412986198693e-20 -179.99924671275849 ;
	setAttr ".bps" -type "matrix" -0.71454328442706083 -0.69920869889477444 -0.023132013964741089 0
		 0.055968188568662557 -0.02417405299094447 -0.99813985845187736 0 0.69734887721178074 -0.7145087896953175 0.056406851530655083 0
		 -27.196042736499741 143.29158642587561 -2.2077523363564451 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperArm_01_rib2JNT" -p "R_upperArm_01_JNT";
	rename -uid "07EB8B51-4AD6-BA26-4660-8EA5855A6C45";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -19.01524999999998 -0.00025000000078989615 -2.6645352591003757e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000001279 -4.8531412986198705e-20 -179.99924671276514 ;
	setAttr ".bps" -type "matrix" -0.71454328442697967 -0.69920869889485759 -0.023132013964734528 0
		 0.055968188568679973 -0.024174052990962317 -0.99813985845187603 0 0.69734887721186256 -0.71450878969523557 0.056406851530682596 0
		 -32.630930412650173 137.97333514075248 -2.3836967477888691 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperArm_01_rib3JNT" -p "R_upperArm_01_JNT";
	rename -uid "817E451E-4F8B-8E20-26CB-D8870998CAB4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -26.621350000000007 -0.00035000000046636615 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000002984 0 -179.99924671278768 ;
	setAttr ".bps" -type "matrix" -0.71454328442670534 -0.6992086988951387 -0.023132013964712334 0
		 0.055968188568700637 -0.024174052990983495 -0.99813985845187414 0 0.69734887721214189 -0.71450878969495968 0.056406851530721391 0
		 -38.065818088798686 132.65508385562734 -2.5596411592211359 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperLeg_01_JNT" -p "C_hip_01_JNT";
	rename -uid "0B68F8B2-4259-79C7-7B00-DC9F4ECEC0ED";
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
createNode joint -n "L_lowerLeg_01_JNT" -p "L_upperLeg_01_JNT";
	rename -uid "E969BE3E-4722-1864-ACE4-5491FC0B6CA4";
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
createNode joint -n "L_lowerLeg_02_endJNT" -p "L_lowerLeg_01_JNT";
	rename -uid "B36D2AC2-44D6-D306-C089-CC88AE54EE1E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 42.189399999999992 -1.1102230246251565e-16 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 17.150787097976934 11.217261827759259 -0.91527773846706939 1;
createNode joint -n "L_foot_01_JNT" -p "L_lowerLeg_02_endJNT";
	rename -uid "E93A618A-4020-1D34-D405-9186B2692B13";
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
createNode joint -n "L_foot_02_JNT" -p "L_foot_01_JNT";
	rename -uid "B72A189E-4F03-D11E-29E6-9CB773927EFD";
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
createNode joint -n "L_foot_03_endJNT" -p "L_foot_02_JNT";
	rename -uid "DC2D0F7A-4F7E-EE80-3581-5EA8E6438800";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 9.5399 -1.7763568394002505e-15 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 19.991175272664378 0.14169543621804426 22.506865441149397 1;
createNode joint -n "L_lowerLeg_01_rib0JNT" -p "L_lowerLeg_01_JNT";
	rename -uid "7FA6642A-4361-AE96-9B72-CA89AF6CC5B1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 5.2736749999999759 -7.9936057773011271e-15 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999929 0 0 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.98856938201123257 0.098949956683044904 -0.11375184843488519 0 0.11964767995437244 -0.055826330407473028 0.99124560705950771 0
		 13.764383547618678 47.893964963438229 1.5590848798699426 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_lowerLeg_01_rib1JNT" -p "L_lowerLeg_01_JNT";
	rename -uid "22923BDF-4267-E8A1-6E13-2A841D42A518";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 15.821024999999977 -3.1086244689504383e-15 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999972 0 0 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.98856938201123246 0.098949956683044932 -0.11375184843488584 0 0.11964767995437309 -0.055826330407472959 0.99124560705950759 0
		 14.731927419149606 37.414906924672806 0.85212413177365653 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_lowerLeg_01_rib2JNT" -p "L_lowerLeg_01_JNT";
	rename -uid "CE84172A-40EA-23B2-D19C-06BDC4B5EADF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 26.368374999999993 2.2204460492503131e-16 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.98856938201123246 0.098949956683044973 -0.1137518484348865 0 0.11964767995437375 -0.055826330407472896 0.99124560705950759 0
		 15.699471290680535 26.935848885907379 0.14516338367736803 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_lowerLeg_01_rib3JNT" -p "L_lowerLeg_01_JNT";
	rename -uid "2C9F98C3-41D3-A515-E547-6991E82E973A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 36.915724999999988 9.9920072216264089e-16 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.98856938201123246 0.098949956683044973 -0.1137518484348865 0 0.11964767995437375 -0.055826330407472896 0.99124560705950759 0
		 16.66701516221147 16.456790847141974 -0.56179736441892247 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperLeg_01_rib0JNT" -p "L_upperLeg_01_JNT";
	rename -uid "86390202-4557-2E6E-9FEE-90AFD42FE28E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.6109875000000216 0 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.98856938201123246 0.098949956683044973 -0.11375184843488606 0 0.10949094408245363 0.047492860074365796 0.99285253759351888 0
		 9.2097514514816492 92.173111747852573 0.49404565673976358 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperLeg_01_rib1JNT" -p "L_upperLeg_01_JNT";
	rename -uid "514A84BF-481B-A83A-189D-BA853F51C719";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 16.832962500000008 1.7763568394002505e-15 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.98856938201123246 0.098949956683044946 -0.1137518484348865 0 0.10949094408245408 0.047492860074365838 0.99285253759351888 0
		 10.372854354444955 81.01893524355782 0.89933697021928816 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperLeg_01_rib2JNT" -p "L_upperLeg_01_JNT";
	rename -uid "05A1F7EE-422A-19E5-37C7-EDB39F6468ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 28.054937500000008 3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.98856938201123246 0.098949956683044946 -0.1137518484348865 0 0.10949094408245408 0.047492860074365838 0.99285253759351888 0
		 11.535957257408255 69.864758739263053 1.3046282836988141 1;
	setAttr ".radi" 0.8;
createNode joint -n "L_upperLeg_01_rib3JNT" -p "L_upperLeg_01_JNT";
	rename -uid "6572BAD5-4C8D-F5A1-3F24-DBBCD0A5AA7E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 39.276912500000009 4.4408920985006262e-15 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.98856938201123246 0.098949956683044946 -0.1137518484348865 0 0.10949094408245408 0.047492860074365838 0.99285253759351888 0
		 12.699060160371559 58.710582234968292 1.7099195971783387 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperLeg_01_JNT" -p "C_hip_01_JNT";
	rename -uid "1033B547-4EA2-E129-2AFB-D7ADC96B4396";
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
createNode joint -n "R_lowerLeg_01_JNT" -p "R_upperLeg_01_JNT";
	rename -uid "E421EEB0-4688-3960-AEF2-D6A7129AA1A7";
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
createNode joint -n "R_lowerLeg_02_endJNT" -p "R_lowerLeg_01_JNT";
	rename -uid "E1B7AFEA-4BD8-927B-BB4D-C5A415632EEF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -42.189399999999971 3.3306690738754696e-15 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.091733358963365486 0.99352520221239515 0.067027333395546645 0
		 0.11964770529926022 0.05582632787059906 -0.99124560414314367 0 -0.9885693791888962 0.098949955458826677 -0.11375187402753628 0
		 -17.150786986502222 11.217261816601301 -0.91527772564000243 1;
createNode joint -n "R_foot_01_JNT" -p "R_lowerLeg_02_endJNT";
	rename -uid "1447C5E9-4DA0-542B-7CE9-4DB29465BECE";
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
createNode joint -n "R_foot_02_JNT" -p "R_foot_01_JNT";
	rename -uid "8653A034-46DA-921F-6ED2-05A4C04619FD";
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
createNode joint -n "R_foot_03_endJNT" -p "R_foot_02_JNT";
	rename -uid "4EC48420-47FD-F47B-4B41-1091C8FC3949";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -9.5399 7.460698725481052e-14 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.1124596683270969 0.35688515442267199 -0.92735419854145529 0
		 0.042964472249414506 -0.93414826797072503 -0.35428952506618616 0 -0.99272699022646127 -1.2479044593370443e-09 -0.12038738669774059 0
		 -19.99117575098116 0.14169548499065021 22.506865410792116 1;
createNode joint -n "R_lowerLeg_01_rib0JNT" -p "R_lowerLeg_01_JNT";
	rename -uid "00968932-4092-BB72-182A-87B1E391458A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.2736750000000043 -1.2323475573339238e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999972 0 179.99999999999994 ;
	setAttr ".bps" -type "matrix" -0.091733358963365361 -0.99352520221239504 -0.067027333395547645 0
		 -0.9885693791888962 0.098949955458826649 -0.11375187402753584 0 0.11964770529925987 0.055826327870600108 -0.99124560414314355 0
		 -13.764383533684345 47.893964962043434 1.5590848814733265 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_lowerLeg_01_rib1JNT" -p "R_lowerLeg_01_JNT";
	rename -uid "B804042A-4487-058C-DD72-9FBC001B2758";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -15.821024999999999 -2.9976021664879227e-15 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 0 179.99999999999997 ;
	setAttr ".bps" -type "matrix" -0.091733358963365416 -0.99352520221239515 -0.067027333395547201 0
		 -0.9885693791888962 0.098949955458826663 -0.11375187402753606 0 0.11964770529926005 0.055826327870599643 -0.99124560414314367 0
		 -14.731927377346594 37.414906920488534 0.85212413658379904 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_lowerLeg_01_rib2JNT" -p "R_lowerLeg_01_JNT";
	rename -uid "3BE2E472-453D-2A32-C034-CDAC48CB2570";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -26.368374999999975 7.7715611723760958e-16 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000014 0 180 ;
	setAttr ".bps" -type "matrix" -0.091733358963365472 -0.99352520221239515 -0.06702733339554677 0
		 -0.9885693791888962 0.098949955458826691 -0.1137518740275365 0 0.11964770529926046 0.055826327870599164 -0.99124560414314367 0
		 -15.699471221008844 26.935848878933655 0.14516339169427805 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_lowerLeg_01_rib3JNT" -p "R_lowerLeg_01_JNT";
	rename -uid "BF0EC1FB-438A-B664-7A71-B19F21EB3056";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -36.915724999999966 2.886579864025407e-15 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 0 179.99999999999997 ;
	setAttr ".bps" -type "matrix" -0.091733358963365416 -0.99352520221239515 -0.067027333395547201 0
		 -0.9885693791888962 0.098949955458826663 -0.11375187402753606 0 0.11964770529926005 0.055826327870599643 -0.99124560414314367 0
		 -16.667015064671098 16.456790837378755 -0.56179735319524271 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperLeg_01_rib0JNT" -p "R_upperLeg_01_JNT";
	rename -uid "C9B47C67-42AE-FB9D-4189-76A1A5E314FF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -5.6109875000000358 0 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000028 0 180 ;
	setAttr ".bps" -type "matrix" -0.10364511620844839 -0.99395841679336883 0.036115863159516634 0
		 -0.9885693791888962 0.098949955458826649 -0.11375187402753673 0 0.10949096956469796 -0.047492862624987447 -0.99285253466134971 0
		 -9.209751451481651 92.173111747852559 0.49404565673976109 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperLeg_01_rib1JNT" -p "R_upperLeg_01_JNT";
	rename -uid "8FC69BE5-4140-4456-3AC9-C99496E6BA4D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -16.832962500000022 0 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000057 0 -180 ;
	setAttr ".bps" -type "matrix" -0.10364511620844842 -0.99395841679336883 0.036115863159516884 0
		 -0.98856937918889609 0.098949955458826622 -0.11375187402753738 0 0.10949096956469859 -0.047492862624987767 -0.99285253466134959 0
		 -10.372854354444959 81.018935243557806 0.89933697021927783 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperLeg_01_rib2JNT" -p "R_upperLeg_01_JNT";
	rename -uid "388240C7-4AAE-B799-3166-108D0D963CD6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -28.054937500000023 -8.8817841970012523e-16 1.0658141036401503e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000057 0 180 ;
	setAttr ".bps" -type "matrix" -0.10364511620844839 -0.99395841679336883 0.036115863159516634 0
		 -0.98856937918889609 0.098949955458826622 -0.11375187402753738 0 0.10949096956469861 -0.047492862624987517 -0.99285253466134959 0
		 -11.53595725740827 69.864758739263038 1.3046282836987961 1;
	setAttr ".radi" 0.8;
createNode joint -n "R_upperLeg_01_rib3JNT" -p "R_upperLeg_01_JNT";
	rename -uid "8B1772E4-4DBA-117D-A8D6-728B56B58DEC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -39.276912500000037 8.8817841970012523e-16 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 0 180 ;
	setAttr ".bps" -type "matrix" -0.10364511620844839 -0.99395841679336883 0.036115863159516634 0
		 -0.9885693791888962 0.098949955458826691 -0.11375187402753606 0 0.1094909695646973 -0.047492862624987385 -0.99285253466134971 0
		 -12.699060160371566 58.710582234968264 1.7099195971783137 1;
	setAttr ".radi" 0.8;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
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
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 15 ".st";
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
	setAttr -s 16 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 74 ".u";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 13 ".r";
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
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -k on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -cb on ".pff";
	setAttr -cb on ".peie";
	setAttr -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -cb on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".mbso";
	setAttr -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr -k on ".rcp";
	setAttr -k on ".icp";
	setAttr -k on ".ocp";
	setAttr -cb on ".hbl";
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
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "G:/FileManager/OCIO/aces_1.0.3/config.ocio";
	setAttr ".vtn" -type "string" "sRGB (ACES)";
	setAttr ".wsn" -type "string" "ACES - ACEScg";
	setAttr ".otn" -type "string" "sRGB (ACES)";
	setAttr ".potn" -type "string" "sRGB (ACES)";
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
connectAttr "C_hip_01_JNT.s" "C_spine_01_JNT.is";
connectAttr "C_spine_01_JNT.s" "C_spine_02_JNT.is";
connectAttr "C_spine_02_JNT.s" "C_spine_03_JNT.is";
connectAttr "C_spine_03_JNT.s" "C_spine_04_JNT.is";
connectAttr "C_spine_04_JNT.s" "C_spine_05_JNT.is";
connectAttr "C_spine_05_JNT.s" "C_spine_06_JNT.is";
connectAttr "C_spine_06_JNT.s" "C_spine_07_JNT.is";
connectAttr "C_spine_07_JNT.s" "C_spine_08_endJNT.is";
connectAttr "C_spine_08_endJNT.s" "C_chest_01_JNT.is";
connectAttr "C_chest_01_JNT.s" "C_chest_01_endJNT.is";
connectAttr "C_chest_01_endJNT.s" "C_neck_01_JNT.is";
connectAttr "C_neck_01_JNT.s" "C_neck_01_endJNT.is";
connectAttr "C_neck_01_endJNT.s" "C_head_01_JNT.is";
connectAttr "C_head_01_JNT.s" "C_head_02_endJNT.is";
connectAttr "C_head_01_JNT.s" "L_socket_01_JNT.is";
connectAttr "L_socket_01_JNT.s" "L_eye_01_JNT.is";
connectAttr "L_eye_01_JNT.s" "L_pupil_01_JNT.is";
connectAttr "C_head_01_JNT.s" "R_socket_01_JNT.is";
connectAttr "R_socket_01_JNT.s" "R_eye_01_JNT.is";
connectAttr "R_eye_01_JNT.s" "R_pupil_01_JNT.is";
connectAttr "C_neck_01_JNT.s" "C_neck_01_rib2JNT.is";
connectAttr "C_neck_01_JNT.s" "C_neck_01_rib1JNT.is";
connectAttr "C_neck_01_JNT.s" "C_neck_01_rib0JNT.is";
connectAttr "C_chest_01_JNT.s" "L_clavicle_01_JNT.is";
connectAttr "L_clavicle_01_JNT.s" "L_upperArm_01_JNT.is";
connectAttr "L_upperArm_01_JNT.s" "L_lowerArm_01_JNT.is";
connectAttr "L_lowerArm_01_JNT.s" "L_lowerArm_02_endJNT.is";
connectAttr "L_hand_01_JNT.s" "L_fingerThumb_01_JNT.is";
connectAttr "L_fingerThumb_01_JNT.s" "L_fingerThumb_02_JNT.is";
connectAttr "L_fingerThumb_02_JNT.s" "L_fingerThumb_03_JNT.is";
connectAttr "L_fingerThumb_03_JNT.s" "L_fingerThumb_04_endJNT.is";
connectAttr "L_hand_01_JNT.s" "L_fingerRing_01_JNT.is";
connectAttr "L_fingerRing_01_JNT.s" "L_fingerRing_02_JNT.is";
connectAttr "L_fingerRing_02_JNT.s" "L_fingerRing_03_JNT.is";
connectAttr "L_fingerRing_03_JNT.s" "L_fingerRing_04_JNT.is";
connectAttr "L_fingerRing_04_JNT.s" "L_fingerRing_05_endJNT.is";
connectAttr "L_hand_01_JNT.s" "L_fingerPinky_01_JNT.is";
connectAttr "L_fingerPinky_01_JNT.s" "L_fingerPinky_02_JNT.is";
connectAttr "L_fingerPinky_02_JNT.s" "L_fingerPinky_03_JNT.is";
connectAttr "L_fingerPinky_03_JNT.s" "L_fingerPinky_04_JNT.is";
connectAttr "L_fingerPinky_04_JNT.s" "L_fingerPinky_05_endJNT.is";
connectAttr "L_hand_01_JNT.s" "L_handEnd_01_endJNT.is";
connectAttr "L_hand_01_JNT.s" "L_fingerMiddle_01_JNT.is";
connectAttr "L_fingerMiddle_01_JNT.s" "L_fingerMiddle_02_JNT.is";
connectAttr "L_fingerMiddle_02_JNT.s" "L_fingerMiddle_03_JNT.is";
connectAttr "L_fingerMiddle_03_JNT.s" "L_fingerMiddle_04_JNT.is";
connectAttr "L_fingerMiddle_04_JNT.s" "L_fingerMiddle_05_endJNT.is";
connectAttr "L_hand_01_JNT.s" "L_fingerIndex_01_JNT.is";
connectAttr "L_fingerIndex_01_JNT.s" "L_fingerIndex_02_JNT.is";
connectAttr "L_fingerIndex_02_JNT.s" "L_fingerIndex_03_JNT.is";
connectAttr "L_fingerIndex_03_JNT.s" "L_fingerIndex_04_JNT.is";
connectAttr "L_fingerIndex_04_JNT.s" "L_fingerIndex_05_endJNT.is";
connectAttr "L_lowerArm_01_JNT.s" "L_lowerArm_01_rib1JNT.is";
connectAttr "L_lowerArm_01_JNT.s" "L_lowerArm_01_rib2JNT.is";
connectAttr "L_lowerArm_01_JNT.s" "L_lowerArm_01_rib3JNT.is";
connectAttr "L_lowerArm_01_JNT.s" "L_lowerArm_01_rib0JNT.is";
connectAttr "L_upperArm_01_JNT.s" "L_upperArm_01_rib0JNT.is";
connectAttr "L_upperArm_01_JNT.s" "L_upperArm_01_rib1JNT.is";
connectAttr "L_upperArm_01_JNT.s" "L_upperArm_01_rib2JNT.is";
connectAttr "L_upperArm_01_JNT.s" "L_upperArm_01_rib3JNT.is";
connectAttr "C_chest_01_JNT.s" "R_clavicle_01_JNT.is";
connectAttr "R_clavicle_01_JNT.s" "R_upperArm_01_JNT.is";
connectAttr "R_upperArm_01_JNT.s" "R_lowerArm_01_JNT.is";
connectAttr "R_lowerArm_01_JNT.s" "R_lowerArm_02_endJNT.is";
connectAttr "R_hand_01_JNT.s" "R_fingerThumb_01_JNT.is";
connectAttr "R_fingerThumb_01_JNT.s" "R_fingerThumb_02_JNT.is";
connectAttr "R_fingerThumb_02_JNT.s" "R_fingerThumb_03_JNT.is";
connectAttr "R_fingerThumb_03_JNT.s" "R_fingerThumb_04_endJNT.is";
connectAttr "R_hand_01_JNT.s" "R_fingerRing_01_JNT.is";
connectAttr "R_fingerRing_01_JNT.s" "R_fingerRing_02_JNT.is";
connectAttr "R_fingerRing_02_JNT.s" "R_fingerRing_03_JNT.is";
connectAttr "R_fingerRing_03_JNT.s" "R_fingerRing_04_JNT.is";
connectAttr "R_fingerRing_04_JNT.s" "R_fingerRing_05_endJNT.is";
connectAttr "R_hand_01_JNT.s" "R_fingerPinky_01_JNT.is";
connectAttr "R_fingerPinky_01_JNT.s" "R_fingerPinky_02_JNT.is";
connectAttr "R_fingerPinky_02_JNT.s" "R_fingerPinky_03_JNT.is";
connectAttr "R_fingerPinky_03_JNT.s" "R_fingerPinky_04_JNT.is";
connectAttr "R_fingerPinky_04_JNT.s" "R_fingerPinky_05_endJNT.is";
connectAttr "R_hand_01_JNT.s" "R_handEnd_01_endJNT.is";
connectAttr "R_hand_01_JNT.s" "R_fingerMiddle_01_JNT.is";
connectAttr "R_fingerMiddle_01_JNT.s" "R_fingerMiddle_02_JNT.is";
connectAttr "R_fingerMiddle_02_JNT.s" "R_fingerMiddle_03_JNT.is";
connectAttr "R_fingerMiddle_03_JNT.s" "R_fingerMiddle_04_JNT.is";
connectAttr "R_fingerMiddle_04_JNT.s" "R_fingerMiddle_05_endJNT.is";
connectAttr "R_hand_01_JNT.s" "R_fingerIndex_01_JNT.is";
connectAttr "R_fingerIndex_01_JNT.s" "R_fingerIndex_02_JNT.is";
connectAttr "R_fingerIndex_02_JNT.s" "R_fingerIndex_03_JNT.is";
connectAttr "R_fingerIndex_03_JNT.s" "R_fingerIndex_04_JNT.is";
connectAttr "R_fingerIndex_04_JNT.s" "R_fingerIndex_05_endJNT.is";
connectAttr "R_lowerArm_01_JNT.s" "R_lowerArm_01_rib1JNT.is";
connectAttr "R_lowerArm_01_JNT.s" "R_lowerArm_01_rib0JNT.is";
connectAttr "R_lowerArm_01_JNT.s" "R_lowerArm_01_rib2JNT.is";
connectAttr "R_lowerArm_01_JNT.s" "R_lowerArm_01_rib3JNT.is";
connectAttr "R_upperArm_01_JNT.s" "R_upperArm_01_rib0JNT.is";
connectAttr "R_upperArm_01_JNT.s" "R_upperArm_01_rib1JNT.is";
connectAttr "R_upperArm_01_JNT.s" "R_upperArm_01_rib2JNT.is";
connectAttr "R_upperArm_01_JNT.s" "R_upperArm_01_rib3JNT.is";
connectAttr "C_hip_01_JNT.s" "L_upperLeg_01_JNT.is";
connectAttr "L_upperLeg_01_JNT.s" "L_lowerLeg_01_JNT.is";
connectAttr "L_lowerLeg_01_JNT.s" "L_lowerLeg_02_endJNT.is";
connectAttr "L_foot_02_JNT.s" "L_foot_03_endJNT.is";
connectAttr "L_lowerLeg_01_JNT.s" "L_lowerLeg_01_rib0JNT.is";
connectAttr "L_lowerLeg_01_JNT.s" "L_lowerLeg_01_rib1JNT.is";
connectAttr "L_lowerLeg_01_JNT.s" "L_lowerLeg_01_rib2JNT.is";
connectAttr "L_lowerLeg_01_JNT.s" "L_lowerLeg_01_rib3JNT.is";
connectAttr "L_upperLeg_01_JNT.s" "L_upperLeg_01_rib0JNT.is";
connectAttr "L_upperLeg_01_JNT.s" "L_upperLeg_01_rib1JNT.is";
connectAttr "L_upperLeg_01_JNT.s" "L_upperLeg_01_rib2JNT.is";
connectAttr "L_upperLeg_01_JNT.s" "L_upperLeg_01_rib3JNT.is";
connectAttr "C_hip_01_JNT.s" "R_upperLeg_01_JNT.is";
connectAttr "R_upperLeg_01_JNT.s" "R_lowerLeg_01_JNT.is";
connectAttr "R_lowerLeg_01_JNT.s" "R_lowerLeg_02_endJNT.is";
connectAttr "R_foot_02_JNT.s" "R_foot_03_endJNT.is";
connectAttr "R_lowerLeg_01_JNT.s" "R_lowerLeg_01_rib0JNT.is";
connectAttr "R_lowerLeg_01_JNT.s" "R_lowerLeg_01_rib1JNT.is";
connectAttr "R_lowerLeg_01_JNT.s" "R_lowerLeg_01_rib2JNT.is";
connectAttr "R_lowerLeg_01_JNT.s" "R_lowerLeg_01_rib3JNT.is";
connectAttr "R_upperLeg_01_JNT.s" "R_upperLeg_01_rib0JNT.is";
connectAttr "R_upperLeg_01_JNT.s" "R_upperLeg_01_rib1JNT.is";
connectAttr "R_upperLeg_01_JNT.s" "R_upperLeg_01_rib2JNT.is";
connectAttr "R_upperLeg_01_JNT.s" "R_upperLeg_01_rib3JNT.is";
// End of new.ma
