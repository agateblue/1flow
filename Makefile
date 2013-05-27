runable:
	fab local runable

fullrunable:
	fab test runable
	fab prod runable

test-fastdeploy:
	fab test fastdeploy

prod-fastdeploy:
	fab prod fastdeploy

#runapp:
#	SPARKS_DJANGO_SETTINGS=chani_app ./manage.py runserver 0.0.0.0:8000

runserver:
	honcho -f Procfile.development start

run: runserver

test: tests

tests:
	#REUSE_DB=1 ./manage.py test oneflow
	./manage.py test oneflow --noinput

shell:
	./manage.py shell

#shellapp:
#	SPARKS_DJANGO_SETTINGS=chani_app ./manage.py shell

messages:
	fab local sdf.makemessages

compilemessages:
	fab local sdf.compilemessages

update-requirements:
	(cd config && pip-dump)

requirements:
	fab local sdf.requirements

syncdb:
	fab local sdf.syncdb
	fab local sdf.migrate

test-restart:
	fab test sdf.restart_services

prod-restart:
	fab prod sdf.restart_services

fixtures:
	@find . -name '*.json' -path '*/fixtures/*'
