        if price < 0:
            raise ValueError("금액은 0원 이상이어야 합니다.")
        if not 1 <= day <= 31:
            raise ValueError("결제일은 1일부터 31일 사이여야 합니다.")
        if category_text not in category_options:
            raise ValueError("카테고리를 선택해 주세요.")
        return name, price, day, category_options[category_text]

    def selected_index():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("선택 필요", "목록에서 구독을 먼저 선택해 주세요.", parent=sub_window)
            return None
        return int(selected[0])

    def fill_from_selection(event=None):
        selected = tree.selection()
        if not selected:
            return
        sub = sub_manager.sub_list[int(selected[0])]
        for entry, value in ((name_entry, sub.name), (price_entry, sub.price), (day_entry, sub.day)):
            entry.delete(0, END)
            entry.insert(0, str(value))
        for text, key in category_options.items():
            if key == sub.category:
                category_box.set(text)
                break

    def add_subscription():
        try:
            name, price, day, category = read_inputs()
            sub_manager.add_register(name, price, day, category)
        except (ValueError, TypeError) as error:
            messagebox.showerror("입력 오류", str(error), parent=sub_window)
            return
        save_data()
        refresh_list()
        clear_inputs()

    def update_subscription():
        index = selected_index()
        if index is None:
            return
        try:
            name, price, day, category = read_inputs()
        except ValueError as error:
            messagebox.showerror("입력 오류", str(error), parent=sub_window)
            return
        sub = sub_manager.sub_list[index]
        sub.name, sub.price, sub.day, sub.category = name, price, day, category
        save_data()
        refresh_list()
        clear_inputs()

    def delete_subscription():
        index = selected_index()
        if index is None:
            return
        name = sub_manager.sub_list[index].name
        if not messagebox.askyesno("삭제 확인", f"'{name}' 구독을 삭제할까요?", parent=sub_window):
            return
        del sub_manager.sub_list[index]
        save_data()
        refresh_list()
        clear_inputs()

    action_frame = Frame(sub_window)
    action_frame.pack(pady=8)
    Button(action_frame, text="등록", width=12, command=add_subscription).pack(side=LEFT, padx=5)
    Button(action_frame, text="수정", width=12, command=update_subscription).pack(side=LEFT, padx=5)
    Button(action_frame, text="삭제", width=12, command=delete_subscription).pack(side=LEFT, padx=5)
    Button(action_frame, text="새로고침", width=12, command=refresh_list).pack(side=LEFT, padx=5)

    tree.pack(fill=BOTH, expand=True, padx=18, pady=(5, 14))
    tree.bind("<<TreeviewSelect>>", fill_from_selection)
    refresh_list()


def open_expense():
    expense_window = Toplevel(window)
    expense_window.title("지출 관리")
    expense_window.geometry("400x300")
    Label(expense_window, text="지출 관리 (추후 구현)", font=("맑은 고딕", 15)).pack(pady=25)


# 데이터 복원은 창 생성 후, 버튼 생성 전에 수행
load_data()

# 기존 이미지 버튼 유지
start_image_1 = PhotoImage(file=str(BASE_DIR / "image" / "subscription_button.png"))
start_image_2 = PhotoImage(file=str(BASE_DIR / "image" / "expense_button.png"))
start_image_1 = start_image_1.subsample(2, 2)
start_image_2 = start_image_2.subsample(2, 2)

Button(window, image=start_image_1, command=open_subscription,
       borderwidth=0, highlightthickness=0).pack(pady=5)
Button(window, image=start_image_2, command=open_expense,
       borderwidth=0, highlightthickness=0).pack(pady=8)

window.mainloop()
