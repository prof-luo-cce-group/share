try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

field_case = EnSightReader( CaseFileName='casefilepath/field.case' )

AnimationScene1 = GetAnimationScene()
AnimationScene1.PlayMode = 'Snap To TimeSteps'

field_case.PointArrays = ['rho']

RenderView1 = GetRenderView()
RenderView1.CameraPosition = [0.0, 0.0, 10000.0]
RenderView1.InteractionMode = '2D'
RenderView1.ViewSize = [1280, 768]

DataRepresentation1 = Show()
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.SelectionPointFieldDataArrayName = 'rho'
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'rho')
DataRepresentation1.ScalarOpacityUnitDistance = 0.3468265572687369
DataRepresentation1.ExtractedBlockIndex = 1
DataRepresentation1.ScaleFactor = 0.5900000095367431

a1_rho_PVLookupTable = GetLookupTableForArray( "rho", 1, RGBPoints=[1.0, 0.23, 0.299, 0.754, 2.336859941482544, 0.865, 0.865, 0.865, 3.673719882965088, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a1_rho_PiecewiseFunction = CreatePiecewiseFunction( Points=[1.0, 0.0, 0.5, 0.0, 3.673719882965088, 1.0, 0.5, 0.0] )

DataRepresentation1.ScalarOpacityFunction = a1_rho_PiecewiseFunction
DataRepresentation1.LookupTable = a1_rho_PVLookupTable

a1_rho_PVLookupTable.ScalarOpacityFunction = a1_rho_PiecewiseFunction

RenderView1.CameraPosition = [0.0, 0.0, 16.119100025205046]
RenderView1.CameraClippingRange = [15.957909024952995, 16.360886525583123]
RenderView1.CameraParallelScale = 4.171930076435588

geo_stl_case = EnSightReader( CaseFileName='casefilepath/geo_stl.case' )

DataRepresentation2 = Show()
DataRepresentation2.ScaleFactor = 0.1
DataRepresentation2.ScalarOpacityUnitDistance = 0.8291561935301535
DataRepresentation2.ExtractedBlockIndex = 1
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

RenderView1.CameraClippingRange = [14.962909024952996, 17.613386525583124]

AnimationScene1.AnimationTime = 1.0

a1_rho_PVLookupTable.RGBPoints = [0.4341404139995575, 0.23, 0.299, 0.754, 3.910554990172386, 0.865, 0.865, 0.865, 7.386969566345215, 0.706, 0.016, 0.15]

a1_rho_PiecewiseFunction.Points = [0.4341404139995575, 0.0, 0.5, 0.0, 7.386969566345215, 1.0, 0.5, 0.0]

RenderView1.CameraParallelScale = 2.8494843770477334

SetActiveSource(field_case)
ComputeDerivatives1 = ComputeDerivatives()

ComputeDerivatives1.Scalars = ['POINTS', 'rho']

ComputeDerivatives1.OutputTensorType = 'Nothing'

DataRepresentation3 = Show()
DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation3.SelectionPointFieldDataArrayName = 'rho'
DataRepresentation3.ScalarOpacityFunction = a1_rho_PiecewiseFunction
DataRepresentation3.ColorArrayName = ('POINT_DATA', 'rho')
DataRepresentation3.ScalarOpacityUnitDistance = 0.3468265572687369
DataRepresentation3.LookupTable = a1_rho_PVLookupTable
DataRepresentation3.ExtractedBlockIndex = 1
DataRepresentation3.ScaleFactor = 0.5900000095367431

DataRepresentation1.Visibility = 0

a3_ScalarGradient_PVLookupTable = GetLookupTableForArray( "ScalarGradient", 3, RGBPoints=[1.0, 1.0, 1.0, 1.0, 100.0, 0.0, 0.0, 0.0], VectorMode='Magnitude', NanColor=[1.0, 0.0, 0.0], ColorSpace='RGB', UseLogScale=1, ScalarRangeInitialized=1.0, LockScalarRange=1 )

a3_ScalarGradient_PiecewiseFunction = CreatePiecewiseFunction( Points=[1.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0] )

DataRepresentation3.ColorAttributeType = 'CELL_DATA'
DataRepresentation3.ScalarOpacityFunction = a3_ScalarGradient_PiecewiseFunction
DataRepresentation3.ColorArrayName = ('CELL_DATA', 'ScalarGradient')
DataRepresentation3.AmbientColor = [1.0, 1.0, 1.0]
DataRepresentation3.LookupTable = a3_ScalarGradient_PVLookupTable
DataRepresentation3.CubeAxesColor = [1.0, 1.0, 1.0]

ScalarBarWidgetRepresentation1 = CreateScalarBar( ComponentTitle='', Title='Schlieren', Position2=[0.13000000000000012, 0.49999999999999983], Enabled=1, LabelFontSize=8, LabelColor=[0.0, 0.0, 0.0], LookupTable=a3_ScalarGradient_PVLookupTable, TitleFontSize=8, TitleColor=[0.0, 0.0, 0.0], Position=[0.8255204934055675, 0.046610169491525466] )
GetRenderView().Representations.append(ScalarBarWidgetRepresentation1)

RenderView1.OrientationAxesVisibility = 0
RenderView1.Background2 = [0.0, 0.0, 0.16470588235294117]
RenderView1.RemoteRenderThreshold = 3.0
RenderView1.Background = [1.0, 1.0, 1.0]
RenderView1.CenterAxesVisibility = 0
RenderView1.CameraParallelScale = 2.8494843770477334
RenderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]

DataRepresentation1.CubeAxesColor = [1.0, 1.0, 1.0]
DataRepresentation1.AmbientColor = [1.0, 1.0, 1.0]

DataRepresentation2.CubeAxesColor = [1.0, 1.0, 1.0]
DataRepresentation2.AmbientColor = [1.0, 1.0, 1.0]

WriteImage('vizfilepath/schlieren.png')
a3_ScalarGradient_PVLookupTable.ScalarOpacityFunction = a3_ScalarGradient_PiecewiseFunction




WriteAnimation('vizfilepath/schlieren.avi', Magnification=2, Quality=2, FrameRate=15.000000)

Render()
