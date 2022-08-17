##RULE OF CODE:
1. Every line of log please use this: 
```shell
from django.conf import settings

loger = settings.LOGGER
loger.info("mess", **extra)
```
### For depveloper.
I. Envs.
1. Clone env template to (eg: local.env)`cp -r env.example local.env` or `cat env.example > local.env` and then update values
2. `chmod +x exportenvs.sh && bash exportenvs.sh` or run it directly in the terminal `eval $(grep -v -e '^#' local.env | xargs -I {} echo export \'{}\')`

II. Local Dev.
1. Clean migrate local db ``` make cl```
2. Makemigration  ``` make mk```
3. Migrate  ``` make mi```
4. Superuser ```make su```
5. Create DB Cache ```make cac```
6. Mock data ```make mock```
7. Build and Push image ```make b p```
8. Run server ```make r``` or run server plus ```make ru```
9. Shell plus ```make sh```

# chuthe-api (features draff)
## todos
### scan page
- [ ] alias's data

### aliases main business's
- [ ] crud (logged in require)

### user registry (under 2min )
- [ ] phone
- [ ] social
- [ ] invite
- [ ] auto create default alias

### login
- [ ] 2fa

### user's settings
- [ ] secure login
- [ ] 
- [ ] language 
- [ ] timezone

### encrypt user information 

### enterprises
- [ ] registry unlimited 
- [ ] crud for employee
#### analytics employeer 
- [ ] by months
- [ ] who's scanned 


### billing
- [ ] Plan
