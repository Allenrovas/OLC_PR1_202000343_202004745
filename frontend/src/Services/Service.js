import * as analisis from './APIs/Analisis'
import * as reportes from './APIs/Reporte'
import * as reportesc3d from './APIs/Reportec3d'
import * as analisisc3d from './APIs/Analisisc3d'

export default {
    ...analisis
    ,...reportes
    ,...reportesc3d
    ,...analisisc3d
}