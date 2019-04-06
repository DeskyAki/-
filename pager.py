class Pagination(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=10, maxPageNum=7):
        self.total_count = totalCount             # 数据总个数
        try:
            v = int(currentPage)                  # 当前页
            if v <= 0:
                v = 1
            self.current_page = v                 # 当前页
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum   # 每页显示的行数
        self.max_page_num = maxPageNum            # 最多显示的页面，就是下面显示有几个分页

    def start(self):
        return (self.current_page-1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property     # 自动个本模块里的函数调用加()
    def num_pages(self):     # 总页数
        a, b = divmod(self.total_count, self.per_page_item_num)  # 数据总个数 每页条数
        if b == 0:
            return a
        return a+1

    def pager_num_range(self):  # 所以它是 下面显示分页的 从几到几
        if self.num_pages < self.max_page_num:    # 总页数小于 显示的页数这里是7
            return range(1, self.num_pages+1)
        part = int(self.max_page_num/2)            # 显示分页的一半，取整数
        if self.current_page <= part:              # 当前页小于 显示分页的一半
            return range(1, self.max_page_num+1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages-self.max_page_num+1, self.num_pages+1)
        return range(self.current_page-part, self.current_page+part+1)

    def page_str(self):
        page_list = []
        first = "<li><a href='/index2.html/?p=1'>首页</a></li>"
        page_list.append(first)
        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"  # 显示但点不了
        else:
            prev = "<li><a href='/index2.html/?p=%s'>上一页</a></li>" % (self.current_page-1)
        page_list.append(prev)
        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a  href='/index2.html/?p=%s'>%s</a></li>" % (i, i)   # 赋值给%s
            else:
                temp = "<li><a href='/index2.html/?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='/index2.html/?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_list.append(nex)

        last = "<li><a href='/index2.html/?p=%s'>尾页</a></li>" % (self.num_pages,)
        page_list.append(last)
        return ''.join(page_list)
