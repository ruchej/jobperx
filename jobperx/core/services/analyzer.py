import xlrd
import datetime


STATUS_1 = {
    "status": 1,
    "msg": "В данном документе отсутствуют данные, удовлетворяющие необходимым условиям",
}


class AnalysisExl:
    def __init__(self, obj):
        self.obj = obj
        path = self.obj.xlfile.path
        self.wb = xlrd.open_workbook(path)
        self.sheets = {}
        for i in self.wb.sheet_names():
            sh = self.wb.sheet_by_name(i)
            if sh.ncols == 0:
                break
            col = 0
            cols = {}
            fields = ["before", "after"]
            while col < sh.ncols:
                val = sh.cell(0, col).value
                if not val:
                    break
                if val in fields:
                    cols[val] = col
                    fields.remove(val)
                col += 1
            if len(cols) == 2:
                self.sheets[i] = cols

    def analyze(self):
        if not self.sheets:
            return STATUS_1
        result = {}
        for i in self.sheets:
            before = self._get_data_col(i, self.sheets[i]["before"])
            after = self._get_data_col(i, self.sheets[i]["after"])
            if abs(len(before) - len(after)) != 1:
                return STATUS_1
            num_x = list(set(before) ^ set(after))
            if len(num_x) == 1:
                result[i] = {
                    "status": 0,
                    "msg": f"На листе {i} искомое число Х={num_x[0]}",
                }
        self.obj.result = result
        self.obj.date_end_proc = datetime.datetime.now()
        self.obj.status = "processed"
        self.obj.save()

    def _get_data_col(self, sheet, col):
        sh = self.wb.sheet_by_name(sheet)
        data = []
        row = 1
        while row < sh.nrows:
            val = sh.cell(row, col).value
            if not val:
                break
            data.append(val)
            row += 1
        return data
