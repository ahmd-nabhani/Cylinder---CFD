// Parameters
rOuter = 3.0;
rInner = 0.5;
h = 1.0; // extrusion height
zMin = 0;

// Circular arc points (quarter arcs for inner cylinder)
Point(1) = {0.5, 0, 0, 1};
Point(2) = {0.353553, 0.353553, 0, 1};
Point(3) = {0, 0.5, 0, 1};
Point(4) = {-0.353553, 0.353553, 0, 1};
Point(5) = {-0.5, 0, 0, 1};
Point(6) = {-0.353553, -0.353553, 0, 1};
Point(7) = {0, -0.5, 0, 1};
Point(8) = {0.353553, -0.353553, 0, 1};
Point(9) = {0, 0, 0, 1.0};
//+


//+
Circle(1) = {4, 9, 2};
//+
Circle(2) = {2, 9, 8};
//+
Circle(3) = {8, 9, 6};
//+
Circle(4) = {6, 9, 4};
//+
Dilate {{0, 0, 0}, {2, 2, 0}} {
  Duplicata { Point{1}; Point{2}; Point{3}; Point{4}; Point{5}; Point{6}; Point{7}; Point{8}; Point{9}; Curve{1}; Curve{2}; Curve{3}; Curve{4}; }
}
//+
Line(9) = {2, 11};
//+
Line(10) = {8, 17};
//+
Line(11) = {6, 15};
//+
Line(12) = {4, 13};
//+
Point(18) = {-10, 10, 0, 0.5};
//+
Point(19) = {-10, -10, 0, 0.5};
//+
Point(20) = {25, -10, 0, 0.5};
//+
Point(21) = {25, 10, 0, 0.5};
//+
Line(13) = {18, 21};
//+
Line(14) = {21, 20};
//+
Line(15) = {20, 19};
//+
Line(16) = {19, 18};
//+
Curve Loop(1) = {1, 9, -5, -12};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {8, -12, -4, 11};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {3, 11, -7, -10};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {2, 10, -6, -9};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {13, 14, 15, 16};
//+
Curve Loop(6) = {5, 6, 7, 8};
//+
Plane Surface(5) = {5, 6};
//+
Transfinite Curve {2, 6, 1, 5, 4, 8, 3, 7} = 30 Using Progression 1;
//+
Transfinite Curve {12, 9, 10, 11} = 30 Using Progression 1;
//+
Transfinite Surface {1};
//+
Transfinite Surface {4};
//+
Transfinite Surface {3};
//+
Transfinite Surface {2};
//+
Recombine Surface {1, 4, 3, 2};
//+
Extrude {0, 0, 1} {
  Point{12}; Point{2}; Point{3}; Point{4}; Point{5}; Point{6}; Point{7}; Point{8}; Point{9}; Point{10}; Point{11}; Point{1}; Point{13}; Point{14}; Point{15}; Point{16}; Point{17}; Point{18}; Point{19}; Point{20}; Point{21}; Curve{12}; Curve{2}; Curve{3}; Curve{4}; Curve{5}; Curve{6}; Curve{7}; Curve{8}; Curve{9}; Curve{10}; Curve{11}; Curve{1}; Curve{13}; Curve{14}; Curve{15}; Curve{16}; Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Layers{1}; Recombine;
}
//+
Physical Surface("in") = {101};
//+
Physical Surface("out") = {93};
//+
Physical Surface("up") = {89};
//+
Physical Surface("down") = {97};
//+
Physical Surface("frontAndBack") = {5, 231, 1, 2, 3, 4, 167, 189, 145, 123};
//+
Physical Surface("cylinder") = {85, 53, 49, 45};
//+
Physical Volume("fluid") = {1, 2, 3, 4, 5};
