

letter_list_description='''
                                    <<this api giving the letters to us there is 4 parameter you can pass>>
                                    
                        host/auto/letter/?sender=<user_id>&?reciever=<reciver_id> ==> perform query letters with this sender OR reciver
                        host/auto/letter/?departman=<departman_id> ==> giving all letter by this departman id  
                        host/auto/letter/?status=<o|c>  ==> o statnd for open & c stand for close 
                       
                                                    <<we can perform all above with each other with order in bellow>>
                        host/auto/letter/?sender=<user_id>&?reciever=<reciver_id>&?departman=<departman_id>&?status=<o|c> 
                        ==> sender OR reciver AND departman AND status
                        '''


user_list_description='''
                                    <<this api giving the users to us there is 3 parameter you can pass>>
                                    
                        host/auto/letter/?username=<>&lastname=<>&firstname=<>   

                        if we pass username and lastname and firstname or any combination of this 
                        backend perform OR query filter for each of them we pass 
'''