ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *index =NULL;
        ListNode *head = NULL;
        ListNode *i = l1, *j= l2;
        if(!l1 && !l2)
        {
        	return NULL;
        }
        while(i && j)
        {
        	int insert_val = 0;
        	if(i->val > j->val)
        	{
        		insert_val = j->val;
        		j = j->next;

        	}
        	else{
        		insert_val = i->val;
        		i = i->next;
        	}
        	//cout<<"inser val"<<insert_val<<endl;
        	ListNode *tmp = new ListNode(0);
        	if(!index){
        		index = tmp;
        		head = tmp;
        	}
        	else{
        		index->next = tmp;
        	}
        	tmp->val = insert_val;
        	tmp->next=NULL;
        	index = tmp;

    	}
    	ListNode *leave = i != NULL? i:j;

    	while(leave)
    	{

    		ListNode *tmp = new ListNode(leave->val);
    		if(index){
               index->next = tmp;

                index = tmp;
            }
    		else
            {
    			index = tmp;
    			head = tmp;
            }
    		leave = leave->next;
    	}
    	return head;

    }