from PySide6.QtWidgets import QApplication, QWidget
import sys


def main() -> int:
    app = QApplication(sys.argv)

    window = QWidget()
    window.show()

    return app.exec()


def throwing_main():
    sys.exit(main())


if __name__ == "__main__":
    throwing_main()
