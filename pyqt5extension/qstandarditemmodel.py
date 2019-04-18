# -*- coding: utf-8 -*-
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
import typing


class QStandardItemModelX(QStandardItemModel):

    change_data = pyqtSignal(str, int, str, name="change_data")

    def __init__(self, *args, **kwargs):
        super(QStandardItemModelX, self).__init__(*args, **kwargs)
        self.change_data.connect(self.on_change_data)
        self.header = []

    def update_data(self, colname, row_ix, content):
        # 发射信号，以供在qt线程中更新数据，保证界面自动刷新
        self.change_data.emit(colname, row_ix, content)

    def on_change_data(self, colname, row_ix, content):
        if colname in self.header:
            col_index = self.header.index(colname)
            self.setData(
                self.index(row_ix, col_index),
                content
            )

    def setHorizontalHeaderLabels(self, labels: typing.Iterable[str]):
        super().setHorizontalHeaderLabels(labels)
        self.header = list()
        for i in range(len(labels)):
            self.header.append(labels[i])
