import view
import model


def start():
    user_input=0
    while user_input!=8:
        user_input = view.show_menu()
        match user_input:
            case 1:
                phone_book=model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new=list(view.create_new_contact())
                model.update_phone_book(new)
                view.update_success()
            case 5:
                search=view.find_what()
                result=model.search_contact_far_changes(search)
                confirmation=view.show_and_confirm_changes(result)
                if 'n' not in confirmation: new_contact=list(view.create_new_contact())
                response=model.change_contact(result,confirmation,new_contact)
                view.change_success(response)


            case 6:
                search=view.find_what()
                result=model.search_contact(search)
                confirmation=view.show_and_confirm__deletion(result)
                response=model.delete_contact(result,confirmation)
                view.deletion_success(response)

            case 7:
                search=view.find_what()
                result=model.search_contact(search)
                view.show_contacts(result)

    else:
        view.goodbye()

    
