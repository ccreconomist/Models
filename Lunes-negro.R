
library(quantmod)
library(dplyr)

# Definir los símbolos de los índices bursátiles
indices <- c("^GSPC", "^DJI", "^IXIC", "^FTSE", "^GDAXI", "^FCHI", "^N225", "^HSI", "EEM", "URTH")

# Descargar datos históricos para los índices (cambiar el período a 'minute' o 'hour' para datos intradía)
data_list <- lapply(indices, function(sym) {
  tryCatch({
    # Descargar datos intradía, por ejemplo cada 5 minutos
    data <- getSymbols(sym, src = "yahoo", from = "2024-01-01", to = Sys.Date(), periodicity = "5min", auto.assign = FALSE)
    
    # Convertir los datos en un data frame
    data_df <- data.frame(Date = index(data), Price = Cl(data)) %>%
      mutate(Index = sym)
    
    return(data_df)
  }, error = function(e) {
    message(paste("Error en el símbolo:", sym, "-", e$message))
    return(NULL)
  })
})

# Filtrar data_list para eliminar posibles NULLs
data_list <- Filter(Negate(is.null), data_list)

# Exportar cada data frame a un archivo CSV con fecha y hora
for (i in seq_along(data_list)) {
  file_name <- paste0("data_", indices[i], ".csv")
  write.csv(data_list[[i]], file = file_name, row.names = FALSE)
  message(paste("Archivo guardado:", file_name))
}
install.packages("tidyr")
install.packages("ggplot2")
install.packages("dplyr")
install.packages("plotly")



library(ggplot2)
library(dplyr)
library(tidyr)
library(plotly)


# Lista de archivos CSV
files <- list.files(pattern = "data_.*\\.csv")

# Leer y combinar todos los archivos CSV en un solo data frame
data_combined <- lapply(files, read.csv) %>%
  bind_rows()

# Convertir la columna de fecha en formato Date-Time
data_combined$Date <- as.POSIXct(data_combined$Date, format="%Y-%m-%d %H:%M:%S")

# Asegúrate de que la columna 'Index' es un factor para mejorar la visualización
data_combined$Index <- as.factor(data_combined$Index)
