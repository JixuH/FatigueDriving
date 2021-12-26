import math

import cv2
import numpy as np
import pydicom
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QBrush, QColor, QIcon, QPainter, QPen, QPolygonF
from PyQt5.QtOpenGL import QGLFormat
from PyQt5.QtWidgets import QGraphicsPolygonItem, QGraphicsScene, QGraphicsView


class Ui_EvidenceIm(QtWidgets.QMainWindow):
    def __init__(self,impath,oneinfo):
        super(Ui_EvidenceIm, self).__init__()
        self.impath = impath
        self.oneinfo = oneinfo
    def setupUi(self, Form):
        Form.setObjectName(self.oneinfo)
        Form.resize(979, 584)
        Form.setFixedSize(979, 584)
        self.evidence_im_view = GraphicsView(Form)
        self.evidence_im_view.setGeometry(QtCore.QRect(10, 40, 960, 540))
        self.evidence_im_view.setObjectName("evidence_im_view")
        self.evidence_im_label = QtWidgets.QLabel(Form)
        self.evidence_im_label.setGeometry(QtCore.QRect(10, 10, 971, 21))
        self.evidence_im_label.setObjectName("evidence_im_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        try:
            # 显示图片
            #img = cv_imread()
            img = cv2.imdecode(np.fromfile(self.impath, dtype=np.uint8), -1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            x = img.shape[1]  # 获取图像宽度
            y = img.shape[0]  # 获取图像高度
            frame = QtGui.QImage(img.data, x, y, x*3, QtGui.QImage.Format_RGB888)

            pix = QtGui.QPixmap.fromImage(frame)
            self.item = QtWidgets.QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QtWidgets.QGraphicsScene()  # 创建场景
            self.scene.clear()
            self.scene.addItem(self.item)
            self.scene.update()
            self.evidence_im_view.setScene(self.scene)  # 将场景添加至视图
        except:
            pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.oneinfo))
        self.evidence_im_label.setText(_translate(
            "Form", "<html><head/><body><p>-------------------------------------------------------------------------- <span style=\" font-size:12pt; font-weight:600; color:#000000;\">图像证据</span> ------------------------------------------------------------------------</p></body></html>"))


# 重写GraphicsView类 可拖动、放大、缩小图像
class GraphicsView(QGraphicsView):
    # 背景区域颜色
    backgroundColor = QColor(255, 255, 255)
    def __init__(self, *args, **kwargs):
        super(GraphicsView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # 设置背景颜色
        self.setBackgroundBrush(self.backgroundColor)
        # CacheBackground              缓存背景
        self.setCacheMode(self.CacheBackground)
        # ScrollHandDrag               光标变成指针，拖动鼠标将滚动滚动条。 该模式可以在交互式和非交互式模式下工作
        self.setDragMode(self.ScrollHandDrag)
        # DontSavePainterState         渲染时，QGraphicsView在渲染背景或前景时以及渲染每个项目时保护painter状态
        self.setOptimizationFlag(self.DontSavePainterState)
        # Antialiasing                 抗锯齿
        # TextAntialiasing             文本抗锯齿
        # SmoothPixmapTransform        平滑像素变换算法
        # HighQualityAntialiasing      请改用Antialiasing
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing |
                            QPainter.SmoothPixmapTransform)
        if QGLFormat.hasOpenGL():
            self.setRenderHint(QPainter.HighQualityAntialiasing)
        # AnchorUnderMouse             鼠标当前位置被用作锚点
        self.setResizeAnchor(self.AnchorUnderMouse)
        # IntersectsItemShape          默认，输出列表包含其形状完全包含在选择区域内的项目以及与区域轮廓相交的项目。
        self.setRubberBandSelectionMode(Qt.IntersectsItemShape)
        # AnchorUnderMouse             鼠标当前位置被用作锚点
        self.setTransformationAnchor(self.AnchorUnderMouse)
        # SmartViewportUpdate          QGraphicsView将尝试通过分析需要重绘的区域来找到最佳的更新模式。
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        # 设置场景(显示在屏幕中间)
        self._scene = QGraphicsScene(-180, -90, 360, 180, self)
        self.setScene(self._scene)

    def wheelEvent(self, event):
        # 滑轮事件
        if event.modifiers() & Qt.ControlModifier:
            self.scaleView(math.pow(2.0, -event.angleDelta().y() / 240.0))
            return event.accept()
        super(GraphicsView, self).wheelEvent(event)

    def scaleView(self, scaleFactor):
        factor = self.transform().scale(
            scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()
        if factor < 0.07 or factor > 100:
            return
        self.scale(scaleFactor, scaleFactor)
