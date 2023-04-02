#include <qt5/QtWidgets/QApplication>
#include <qt5/QtWidgets/QWidget>
#include <qt5/QtWidgets/QPushButton>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv); // Initialize the application

        QWidget window; // Create a top-level window
            window.resize(250, 150); // Set the size of the window
                window.setWindowTitle("My App"); // Set the title of the window

                    QPushButton btn("Hello, world!", &window); // Create a button and add it to the window
                        btn.setToolTip("Click me!"); // Set a tooltip for the button
                            btn.resize(btn.sizeHint()); // Set the size of the button to its recommended size
                                btn.move(50, 50); // Set the position of the button within the window

                                    window.show(); // Show the window

                                        return app.exec(); // Enter the main event loop
                                        }
                                        