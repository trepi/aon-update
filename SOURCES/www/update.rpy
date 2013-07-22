
import aon.update.resource


## Comment out this line when finished debugging
reload(aon.update.resource)


resource = aon.update.resource.PackageLists(pkgnarrow='updates', nopkgsmsg='No existen actualizaciones disponibles', action='update_action.rpy', actionlabel='Actualizar')

