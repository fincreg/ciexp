TARGET = hello

all: $(TARGET)

$(TARGET):
	echo '#!/bin/bash' > $(TARGET)
	echo 'echo "Hello World!"' >> $(TARGET)
	chmod +x $(TARGET)

clean:
	rm -f $(TARGET)
	