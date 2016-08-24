  # serializer = WizardSerializer(data=request.data)
        # if serializer.is_valid():
        #     wizard = serializer.save()
        #     print "Wizard PK", wizard.pk
            # return HttpResponse ("Wizard PK", wizard.pk)
            # wizardJson = serializers.serialize('json', [wizard], ensure_ascii=False)
            # print wizardJson
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # print "OK"
        
  
  
  
# new code
 # print "REQUEST.DATA", request.data # output the same 
    # wizard = request.data
    # print "REQUEST.POST", request.POST #output the same
    # try:
        wizard_id = int(request.data.get('id'))
        wizard = Wizard.objects.create(
                      first_name= request.data['first_name'],
                      last_name = request.data['last_name'],
                      company_name = request.data['company_name']
        )
            
        wizardJSON = serializers.serialize('json', [wizard], ensure_ascii=False)
            
        print wizardJSON, type(wizardJSON)
            
        return Response(wizardJSON)
            
    # except ValueError:
        # pass
        #     wizard_id = None

        # try:
        #     wizard = Wizard.objects.get(id=wizard_id)
        #     wizard.first_name = request.data['first_name']
        #     wizard.last_name = request.data['last_name']
        #     wizard.save()
        # except Wizard.DoesNotExist:
        #     Wizard.objects.crate
            
        
        
        # if wizard id is empty, create an object
        # wizard_id = "25"
        
        # if wizard_id == "":
        #     print "OBJECT ID:", request.POST.get('id')
        

        # TODO: If the wizard ID does not exist, create a new wizard.
        #     wizard = Wizard.objects.create(
        #       first_name= request.POST['first_name'],
        #       last_name = request.POST['last_name'],
        #       company_name = request.POST['company_name']
        #     )

    
        #     wizardJSON = serializers.serialize('json', [wizard], ensure_ascii=False)
    
        #     print wizardJSON, type(wizardJSON)
            
        #     return Response(wizardJSON)
        # elif wizard_id != "":
        #     print "OBJECT ID:", wizard_id
        #     # TODO: If the wizard ID already exists, update the existing wizard.
        #     wizard = Wizard.objects.create(
        #           first_name= request.POST('first_name')
        #     )


        #     wizardJSON = serializers.serialize('json', [wizard], ensure_ascii=False)

        #     print wizardJSON, type(wizardJSON)
        
            # return Response(wizardJSON)
                   
  
  
  #test
  
  if wizard_id != "":
            print "OBJECT ID:", wizard_id
            # TODO: If the wizard ID already exists, update the existing wizard.
           
            wizard = Wizard.objects.get(
              first_name= request.POST['first_name'],
              last_name = request.POST['last_name'],
              company_name = request.POST['company_name']
            )
        
            wizardJSON = serializers.serialize('json', [wizard], ensure_ascii=False)

            dict_wizard = ast.literal_eval(wizardJSON) # convert unicode to list
            
            # dict_wizard[0]['first_name'] =  request.data['first_name']
           
            
            print wizardJSON, dict_wizard
         
            return Response(wizardJSON)
            
            




# Script
<script type="text/javascript">
     /*global $*/
    // This will stop Cloud 9 from warning you
    // that '$' does not exist.
    
    $(document).ready(function(){
        
       var timeoutID;
    
        $('#theForm').on('input', function() {
    
            // Wait one second since last input event before
            // calling the saveToDB function.
            
            // clears window time out
            clearTimeout(timeoutID);
            timeoutID = setTimeout(saveToDB, 1000);
    
        });
    
    
        //Serialize the form to JSON object
        $.fn.serializeObject = function(){
                
            var jsonObject = {};
            var formSerializeArray = this.serializeArray(); //serialize the form
            
            // for every item in the serizalize array
            $.each(formSerializeArray, function() {
                  
                if (jsonObject[this.name] !== undefined) {
                        alert("UNDEFINED");
                } else {
                    jsonObject[this.name] =   this.value ;
                }
            });
            
            //reutrn full JSON object
            return jsonObject;
        
            console.log(jsonObject);
        };
    
    
        // Save to the db usign AJAX call
        function saveToDB() {
            
            var $form = $("#theForm");
            var formData = $form.serializeObject();
            var inputID = $("#id");
            // console.log(typeof(formData))
        
            // AJAX call
            $.ajax({
                // Call the "wizard_api_view" 
                url: 'api/wizard/',
                type: "POST",
                data: formData, // serialize the form as JSON
                success: function (data) {
                    // If the data is posted, show success message
                    var parsedData = JSON.parse(data);
                    // console.log(typeof(parsedData));
                    console.log('Successfully posted!', parsedData); 
                    // console.log('Response data:', formData.id);
                    console.log('OBJECT ID:', parsedData[0].pk)
                    inputID.val(parsedData[0].pk); //capture POST request id
                },
                error: function (error) {
                    console.log("ERROR:", error);
                }
            });
        
        }
        
    });

</script>
            
            